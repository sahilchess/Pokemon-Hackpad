import board
import busio
import displayio

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.matrix import DiodeOrientation
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.rgb import RGB, AnimationModes
from kmk.extensions.display import Display, TextEntry
from kmk.extensions.display.ssd1306 import SSD1306

keyboard = KMKKeyboard()

keyboard.col_pins = (board.GP26, board.GP27, board.GP28)
keyboard.row_pins = (board.GP3, board.GP4)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# encoder: ccw, cw, press handled by the matrix
encoder_handler = EncoderHandler()
encoder_handler.pins = ((board.GP2, board.GP1, None),)
encoder_handler.map = [((KC.F20, KC.F19, None),)]
keyboard.modules.append(encoder_handler)

# 2 leds only
rgb = RGB(
    pixel_pin=board.GP29,
    num_pixels=2,
    animation_mode=AnimationModes.SWIRL,
    hue_default=0,
    sat_default=100,
    val_default=100,
)
keyboard.extensions.append(rgb)

# 0.91in 128x32 ssd1306 over i2c, sda gp6 scl gp7
displayio.release_displays()
i2c_bus = busio.I2C(board.GP7, board.GP6)
driver = SSD1306(i2c=i2c_bus, device_address=0x3C)
display = Display(
    entries=[TextEntry(text='pokemon hackpad', x=0, y=0)],
    width=128,
    height=32,
    driver=driver,
)
keyboard.extensions.append(display)

# every key sends an unused f key so input remapper can remap them
keyboard.keymap = [
    [
        KC.F13, KC.F14, KC.F15,
        KC.F16, KC.F17, KC.F18,
    ]
]

if __name__ == '__main__':
    keyboard.go()
