import time
import board
import displayio
from digitalio import DigitalInOut, Pull
from adafruit_debouncer import Debouncer
import neopixel
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

# Compatibility with both CircuitPython 8.x.x and 9.x.x.
# Remove after 8.x.x is no longer a supported release.
try:
    from i2cdisplaybus import I2CDisplayBus
except ImportError:
    from displayio import I2CDisplay as I2CDisplayBus

import terminalio

# can try import bitmap_label below for alternative
from adafruit_display_text import label
import adafruit_displayio_sh1107

displayio.release_displays()
# oled_reset = board.D9

# Use for I2C
i2c = board.I2C()  # uses board.SCL and board.SDA
# i2c = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector on a microcontroller
display_bus = I2CDisplayBus(i2c, device_address=0x3C)

# SH1107 is vertically oriented 64x128
WIDTH = 128
HEIGHT = 64
BORDER = 2

display = adafruit_displayio_sh1107.SH1107(
    display_bus, width=WIDTH, height=HEIGHT, rotation=0
)

time.sleep(1)

# ----- Keypad setup ----- #
switch_a_in = DigitalInOut(board.D5)
switch_b_in = DigitalInOut(board.D6)
switch_a_in.pull = Pull.UP
switch_b_in.pull = Pull.UP
switch_a = Debouncer(switch_a_in)
switch_b = Debouncer(switch_b_in)
switch_a_pressed = False
switch_b_pressed = False

# ----- Key colour setup ----- #
DLIME = 0x33CC33
CYAN = 0x0088DD
WHITE = 0xCCCCCC
BLACK = 0x000000

# Set neopixel colours
pixel_pin = board.D9
pixels = neopixel.NeoPixel(pixel_pin, 2, brightness=1.0)
pixels.fill(BLACK)
time.sleep(0.3)
pixels.fill(WHITE)
time.sleep(0.3)
pixels.fill(BLACK)
time.sleep(0.3)
pixels[0] = DLIME
pixels[1] = CYAN

# ----- Keyboard setup ----- #
keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)  # We're in the US :)

# Make the display context
splash = displayio.Group()
display.root_group = splash

color_bitmap = displayio.Bitmap(WIDTH, HEIGHT, 1)
color_palette = displayio.Palette(1)
color_palette[0] = 0xFFFFFF  # White

bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
splash.append(bg_sprite)

# Draw a smaller inner rectangle in black
inner_bitmap = displayio.Bitmap(WIDTH - BORDER * 2, HEIGHT - BORDER * 2, 1)
inner_palette = displayio.Palette(1)
inner_palette[0] = 0x000000  # Black
inner_sprite = displayio.TileGrid(
    inner_bitmap, pixel_shader=inner_palette, x=BORDER, y=BORDER
)
splash.append(inner_sprite)

# Draw some label text
text = "BinaryKeeb"
text_area = label.Label(
    terminalio.FONT, text=text, scale=2, color=0xFFFFFF, x=6, y=15
)
splash.append(text_area)

text2 = " - ________ - "
text_area2 = label.Label(
    terminalio.FONT, text=text2, scale=1, color=0xFFFFFF, x=20, y=44
)
splash.append(text_area2)


# ----- Binary setup ----- #
bin_str = ""


# ----- Setting up Binary String Display ----- #

def get_bin():
    res = " - "
    res += bin_str
    for i in range(0, 8-len(bin_str)):
        res += "_"
    res += " - "
    return res

tempy = ""

while True:

    switch_a.update()  # Debouncer checks for changes in switch state
    switch_b.update()

    if switch_a.fell and not switch_a_pressed:
        switch_a_pressed = True
        bin_str += "0"
        pixels[0] = WHITE
        tempy = get_bin()
        text_area2.text = tempy.format(time.monotonic())
    if switch_a.rose:
        switch_a_pressed = False
        pixels[0] = DLIME

    if switch_b.fell and not switch_b_pressed:
        switch_b_pressed = True
        bin_str += "1"
        pixels[1] = WHITE
        tempy = get_bin()
        text_area2.text = tempy.format(time.monotonic())
    if switch_b.rose:
        switch_b_pressed = False
        pixels[1] = CYAN

    if len(bin_str) == 8 :
        if (int(bin_str,2) < 41 or int(bin_str,2) > 127) and int(bin_str,2) != 8 and int(bin_str,2) != 27:
            text_area2.text = str("Invalid binary").format(time.monotonic())
        else:
            keyboard_layout.write(chr(int(bin_str, 2)))

            if bin_str == "00001000":
                text_area2.text = str("   BACKSPACE").format(time.monotonic())
            elif bin_str == "00001001":
                text_area2.text = str("     TAB").format(time.monotonic())
            elif bin_str == "00001010":
                text_area2.text = str("    ENTER").format(time.monotonic())
            elif bin_str == "00011011":
                text_area2.text = str("    ESCAPE").format(time.monotonic())
            elif bin_str == "01111111":
                text_area2.text = str("    DELETE").format(time.monotonic())
            else:
                text_area2.text = str("       " + chr(int(bin_str, 2))).format(time.monotonic())
        bin_str = ""
