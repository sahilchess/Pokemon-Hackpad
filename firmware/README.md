# Firmware

This hackpad runs KMK firmware on the XIAO RP2040

## Files


main.py the whole firmware, matrix, encoder, rgb, and oled setup


## Pinout


col0 GP26, col1 GP27, col2 GP28
row0 GP3, row1 GP4
encoder a GP2, encoder b GP1, encoder click is wired into the matrix at row0 col2
rgb data GP29, 3x SK6812 MINI E leds
oled sda GP6, scl GP7, 0.91in 128x32 SSD1306


## Keymap

copy  paste  mute/encoder click
undo  select all  redo

encoder rotate changes volume, rgb boots into swirl mode, oled shows a static text screen

## Setup


install CircuitPython on the XIAO RP2040
copy the kmk library folder from kmk_firmware onto CIRCUITPY
copy main.py onto CIRCUITPY, it runs automatically on boot
