# BinaryKeeb - A Hardware Binary Keyboard

### Welcome to BinaryKeeb!

Binary Keeb ia a mini project of mine, that ive taken up as a starter project to get familiar with Embedded Systems Development.

Its pretty simple. You have two buttons, "One" and "Zero", and you use them to input the character you want, in binary, and once the keyboard recived a full byte - i.e 8 0's and 1's, it send that character to the sytem, as would a normal keyboard.

This project utilises the Adafruit ESP32 Feather V2 as the main board, the Adafruit FeatherWing OLED - 128x64 for the display and finally, the Adafruit NeoKey FeatherWing (Two mechanical keys) for the actual "KeyBoard"

Additionally, it may also be made to run on the Adafruit ESP32-S3 Reverse TFT Feather.


This particular project drew its inspiration originally from the VR game - Job Simulator - It had a very peculiar keyboard, with ony two keys, a zero and a one (It wasnt actually functional though).
