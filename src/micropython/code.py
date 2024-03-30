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
bin_str = ""


# ----- Setting up Binary String Display ----- #

def get_bin():
    res = " - "
    res += bin_str
    for i in 8-len(bin_str):
        res += "_ "
    res += "- "
    return res


# ----- Display setup ----- #
WIDTH = 128
HEIGHT = 64
BORDER = 2
i2c = board.I2C()
display_address = 0x3C
display_bus = displayio.I2CDisplay(i2c, device_address=display_address)
display = adafruit_displayio_sh1107.SH1107(
    display_bus, width=WIDTH, height=HEIGHT, rotation=0
)

splash = displayio.Group()

color_bitmap = displayio.Bitmap(WIDTH, HEIGHT, 1)
color_palette = displayio.Palette(1)
color_palette[0] = 0xFFFFFF  # White

header_text = "Binary Keeb 1.0"
header_area = label.Label(terminalio.FONT, text=header_text, color=0xFFFFFF, x=8, y=8)
splash.append(header_area)
body_text = get_bin()
body_area = label.Label(
    terminalio.FONT, text=body_text, scale=2, color=0xFFFFFF, x=9, y=44
)
splash.append(body_area)


# ----- Setting up Display Refresh Function ----- #

def disp_refresh():
    splash[1].text = get_bin()
    display.refresh()

while True:

    switch_a.update()  # Debouncer checks for changes in switch state
    switch_b.update()

    if switch_a.fell and not switch_a_pressed:
        switch_a_pressed = True
        bin_str += "0"
        pixels[0] = WHITE
    if switch_a.rose:
        switch_a_pressed = False
        pixels[0] = MAGENTA

    if switch_b.fell and not switch_b_pressed:
        switch_b_pressed = True
        bin_str += "1"
        pixels[1] = WHITE
    if switch_b.rose:
        switch_b_pressed = False
        pixels[1] = CYAN

    if len(bin_str) == 8 :
        keyboard.send(chr(int(bin_str, 2)))
        bin_str = ""

    disp_refresh()

