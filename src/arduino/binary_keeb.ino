#include <SPI.h>
#include <Wire.h>
#include <Arduino.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SH110X.h>
#include <Keyboard.h>

#define SCREEN_WIDTH 128
#define SCREEN_HEIGHT 64
#define BUTTON_A 15
#define BUTTON_B 32
#define BUTTON_C 14

#define ZERO_PIN 5
#define ONE_PIN 6

Adafruit_SH1107 display = Adafruit_SH1107(SCREEN_HEIGHT, SCREEN_WIDTH, &Wire);

bool zeroPressed = true;
bool onePressed = true;

unsigned int currentByte = 0;
unsigned int count = 0;

String debugData = "";

void setup() {
  Serial.begin(115200);

  pinMode(ZERO_PIN, INPUT_PULLUP);
  pinMode(ONE_PIN, INPUT_PULLUP);

  pinMode(BUTTON_A, INPUT_PULLUP);
  pinMode(BUTTON_B, INPUT_PULLUP);
  pinMode(BUTTON_C, INPUT_PULLUP);

  Keyboard.begin();

  if (!display.begin(0x3C, true)) {
    Serial.println(F("Display failed to load"));
    for (;;); // go into permanenet loop so we don't break stuff 
  }
  
  drawBits();

}

void loop() {
  delay(10);
  
  if (clicked(&zeroPressed, ZERO_PIN)) {
    addBit(0);
  }
  if (clicked(&onePressed, ONE_PIN)) {
    addBit(1);
  }
}

bool clicked(bool *isPressed, int pin) {
  if (digitalRead(pin) == HIGH && !(*isPressed)) {
    *isPressed = true;
    return true;
  } else if (digitalRead(pin) == LOW) {
    *isPressed = false;
  }

  return false;
}

void addBit(int b) {
  // Shift bits left
  currentByte <<= 1;
  // Modify least significant bit
  currentByte |= b;
  
  count++;

  if (count == 8) {
    Keyboard.write((int)currentByte);
    currentByte = 0;
    count = 0;
  }
  
  drawBits();
}

void drawBits() {
  display.clearDisplay();
  display.setTextSize(2);
  display.setTextColor(SH110X_WHITE);
  display.setCursor(0,8);
  String output = "-";

  for (int i = count; i > 0; i--) {
    output += ((currentByte >> i-1) & 1) == 0 ? "0" : "1";
  }

  for (int i = count; i <= 7; i++) {
    output += "_";
  }

  output += "-";

  display.println(output);
  display.display();
}
