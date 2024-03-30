# BinaryKeeb - A Hardware Binary Keyboard

## Welcome to BinaryKeeb!

Binary Keeb ia a mini project of mine, that ive taken up as a starter project to get familiar with Embedded Systems Development.

## The story behind it?

This particular project drew its inspiration originally from the VR game - Job Simulator - It had a very peculiar keyboard, with ony two keys, a zero and a one (It wasnt actually functional though).

## How does it work?

Its pretty simple. You have two buttons, "One" and "Zero", and you use them to input the character you want, in binary, and once the keyboard has recived a full byte - i.e 8 0's and 1's, it sends that character to the connected sytem, as would a normal keyboard.

## Hardware
This project utilises the [Adafruit ESP32 Feather V2](https://www.adafruit.com/product/5400) as the main board, the [Adafruit FeatherWing OLED - 128x64](https://www.adafruit.com/product/4650) for the display and finally, the [Adafruit NeoKey FeatherWing (Two mechanical keys)](https://www.adafruit.com/product/4979) for the actual "keyboard" (Can also work on the Adafruit ESP32-S3 Reverse TFT Feather)

## Progress

Originally, I had intended for this project to be in Arduino code, as evident [here](/src/arduino/binary_keeb.ino/binary_keeb.ino), however, the Adafruit ESP32 Feather V2 does not have HID support (for the Keyboard.h header to function), hence the project was shifted over to CircuitPython, Adafruit's fork of MicroPython, built for the Adafruit boards.

I have completed most of the code for the keyboard to function properly, and will begin testing once my boards arrive.


## Furure plans?

### Custom PCB and Casing

At a later point of time (most likely in a month or two), I plan on getting a custom pcb printed for this project, as well as getting a case for it either 3D-printed or laser-cut, and make it good-looking

### Wireless BinaryKeeb??

Since the Adafruit ESP32 Feather V2 also has WIFI and Bluetooth, I think I may also make BinaryKeeb into a bluetooth keyboard at a later point, when I successfully complete as a Serial USB Keyboard, and once I secure a power souce to keep the board running while disconnected. Also, that version will be implemented (hopefully) in both Arduino code and CircuitPython (as the board Adafruit ESP32 Feather V2 has implementations in Arduino code to enable it to act aa a bluetooth keyboard)

