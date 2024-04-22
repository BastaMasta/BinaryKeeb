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

Originally, I had intended for this project to be in Arduino code, as evident [here](/src/arduino/binary_keeb.ino), however, the initial board that this project was using was the [Adafruit ESP32 Feather V2](https://www.adafruit.com/product/5400), and that board has no native serial usb support, so my lazy and dumb ass tought that the reason that code wouldn't work was because the board has no implementations for it to act as a keyboard in arduino code, and that it maybe had it in CircuitPython. That is how I spent like 1 week trying to figure out if it was a problem with the board or just me who was dumb (obviously, it was the latter). So, I just built the basic stuff for the keyboard, like detecting switch presses, taking in input and storing it into a binary string, and finally displaying everything on the display.

Later as the esp32 feather v2 had bluetooth, I figured I could make it into a bluetooth keyboard instead of a serial USB one. I think god hates me, as while the board has bluetooth capabilities, there is no scope for me to use its bluetooth capabilities in CircuitPython, as the devs would have to restructure the a whole fricking lot of code just to enable the board to use bluetooth in CP.

So, as I sat there, contemplating what went wrong in my life for me to end up here, while staring into the abyss, simlutaneously suppressing the urge to throw my fridge off the 3rd floor (that was as high as I could go at the hostel), I just looked up which feather boards had native serial USB support, along with which boards had proper bluetooth support, and later placed an order for them.

Basically, I built the keyboard, but it couldnt send output to the computer, and then waited for the [Adafruit Feather RP2040 ](https://www.adafruit.com/product/4884) to arrive (as of 22/04/2024, I am still wating, but to be fair, I placed an order for it like yesterday) and also placed an order for the [Adafruit Feather RP2040 ](https://www.adafruit.com/product/4884) while I was at it, just so that i could have it work as a bluetooth keyboard later as well

If this dosen't work, I might just throw myself off a fricking cliff.

![current atatus image](/assets/binkeeb_pic1.jpeg?raw=true)


## Furure plans?

### Custom PCB and Casing

At a later point of time (most likely in a month or two), I plan on getting a custom pcb printed for this project, as well as getting a case for it either 3D-printed or laser-cut, and make it good-looking

### Wireless BinaryKeeb??

At a later point, I may also make BinaryKeeb into a bluetooth keyboard, with the help of the [Adafruit Feather RP2040 ](https://www.adafruit.com/product/4884), when I successfully complete it as a Serial USB Keyboard, and once I secure a power souce to keep the board running while disconnected.
And also, I may re-write the code as an arduino sketch, just for the sake of having both options, and also so that later I can use another main board instead of the adafruit one I'm using now, like maybe Arduino Nano or such. just for the sake of being able to build the keyboard with whatever board I desire.

## Special Note:
This is, in the end, just a mini project of mine. I dont intend to make a huge fuss out of this, and am doing this just beacus I thought: "Why not?".
And, if you like it, you can reach out to me anytime on discord (bastamasta / BASTAMASTA#6003), and I will be very much happy to connect!

