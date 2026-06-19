import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.rgb import RGB, AnimationModes

keyboard = KMKKeyboard()

keyboard.col_pins = (board.GP26, board.GP27, board.GP28)
keyboard.row_pins = (board.GP3, board.GP4)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

encoder_handler = EncoderHandler()
encoder_handler.pins = ((board.GP2, board.GP7, None),)
keyboard.modules.append(encoder_handler)

rgb = RGB(
    pixel_pin=board.GP29,
    num_pixels=4,
    val_limit=100,
    hue_default=0,
    sat_default=100,
    val_default=100,
    animation_mode=AnimationModes.SWIRL,
)
keyboard.extensions.append(rgb)

# solid color instead of wave, swap animation_mode above to AnimationModes.STATIC
# rgb = RGB(
#     pixel_pin=board.GP29,
#     num_pixels=4,
#     val_limit=100,
#     hue_default=0,
#     sat_default=100,
#     val_default=100,
#     animation_mode=AnimationModes.STATIC,
# )
# keyboard.extensions.append(rgb)

keyboard.keymap = [
    [
        KC.NO, KC.NO, KC.MUTE,
        KC.NO, KC.NO, KC.NO,
    ]
]

encoder_handler.map = [
    ((KC.VOLU, KC.VOLD, KC.NO),),
]

if __name__ == '__main__':
    keyboard.go()


"""
col0, D0, GP26
col1, D1, GP27
col2, D2, GP28
row0, D10, GP3
row1, D9, GP4
ec11a, D8, GP2
ec11b, D5, GP7
rgb_led, D3, GP29

"""
