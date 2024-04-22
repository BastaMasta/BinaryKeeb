# BinaryKeeb - A Hardware Binary Keyboard

## Welcome to BinaryKeeb!

Binary Keeb ia a mini project of mine, that ive taken up as a starter project to get familiar with Embedded Systems Development.

## The story behind it?

This particular project drew its inspiration originally from the VR game - Job Simulator - It had a very peculiar keyboard, with ony two keys, a zero and a one (It wasnt actually functional though).

## How does it work?

Its pretty simple. You have two buttons, "One" and "Zero", and you use them to input the character you want, in binary, and once the keyboard has recived a full byte - i.e 8 0's and 1's, it sends that character to the connected sytem, as would a normal keyboard.

## Hardware
This project utilises the [Adafruit Feather RP2040 ](https://www.adafruit.com/product/4884) as the main board, the [Adafruit FeatherWing OLED - 128x64](https://www.adafruit.com/product/4650) for the display and finally, the [Adafruit NeoKey FeatherWing (Two mechanical keys)](https://www.adafruit.com/product/4979) for the actual "keyboard" (Can also work on the Adafruit ESP32-S3 Reverse TFT Feather)

## Progress

Originally, I had intended for this project to be in Arduino code, as evident [here](/src/arduino/binary_keeb.ino), however, the Adafruit ESP32 Feather V2 does not have HID support (for the Keyboard.h header to function), hence the project was shifted over to CircuitPython, Adafruit's fork of MicroPython, built for the Adafruit boards.

I have completed most of the code for the keyboard to function properly, and will begin testing once my boards arrive.

![current atatus image](/assets/binkeeb_pic1.jpeg?raw=true)


## Furure plans?

### Custom PCB and Casing

At a later point of time (most likely in a month or two), I plan on getting a custom pcb printed for this project, as well as getting a case for it either 3D-printed or laser-cut, and make it good-looking

### Wireless BinaryKeeb??

At a later point, I may also make BinaryKeeb into a bluetooth keyboard, with the help of the [Adafruit Feather 32u4 Bluefruit LE](https://www.adafruit.com/product/2829), when I successfully complete it as a Serial USB Keyboard, and once I secure a power souce to keep the board running while disconnected.
And also, I may re-write the code as an arduino sketch, just for the sake of having both options, and also so that later I can use another main board instead of the adafruit one I'm using now, like maybe Arduino Nano or such. just for the sake of being able to build the keyboard with whatever board I desire.

## Special Note:
This is, in the end, just a mini project of mine. I dont intend to make a huge fuss out of this, and am doing this just beacus I thought: "Why not?".
And, if you like it, you can reach out to me anytime on discord (bastamasta / BASTAMASTA#6003), and I will be very much happy to connect!

