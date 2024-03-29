import time
import board

#  ----- Keyboard Imports -----  #
from digitalio import DigitalInOut, Pull
from adafruit_debouncer import Debouncer
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
import neopixel

#  ----- Display Imports -----  #
import displayio
import terminalio
from adafruit_display_text import label
import adafruit_displayio_sh1107

time.sleep(1)  # Sleep for a bit to avoid a race condition on some systems

#  ----- Keyboard setup -----  #
keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)

# ----- Key setup ----- #
switch_a_in = DigitalInOut(board.D5)
switch_b_in = DigitalInOut(board.D6)
switch_a_in.pull = Pull.UP
switch_b_in.pull = Pull.UP
switch_a = Debouncer(switch_a_in)
switch_b = Debouncer(switch_b_in)
switch_a_pressed = False
switch_b_pressed = False

# ----- NeoPixel setup ----- #
MAGENTA = 0xFF00FF
CYAN = 0x0088DD
WHITE = 0xCCCCCC
BLACK = 0x000000

pixel_pin = board.D9
pixels = neopixel.NeoPixel(pixel_pin, 2, brightness=1.0)
pixels.fill(BLACK)
time.sleep(0.3)
pixels.fill(WHITE)
time.sleep(0.3)
pixels.fill(BLACK)
time.sleep(0.3)
pixels[0] = MAGENTA
pixels[1] = CYAN

# ----- Binary setup ----- #
fin_op = ""

while True:

    switch_a.update()  # Debouncer checks for changes in switch state
    switch_b.update()

    if switch_a.fell and not switch_a_pressed:
        fin_op += "0"
        pixels[0] = WHITE
    if switch_a.rose:
        pixels[0] = MAGENTA

    if switch_b.fell and not switch_b_pressed:
        fin_op += "1"
        pixels[1] = WHITE
    if switch_b.rose:
        pixels[1] = CYAN

    if len(fin_op) == 8 :
        keyboard.send(chr(int(fin_op, 2)))
        fin_op = ""

