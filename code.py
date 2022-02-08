import keypad
import board
import rotaryio
#from adafruit_macropad import MacroPad
import adafruit_matrixkeypad
from digitalio import DigitalInOut
import time
#macropad = MacroPad()
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

keyboard = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(keyboard)
#km = keypad.KeyMatrix(
#    row_pins=(board.P0_22, board.P0_24, board.P0_31),
#    column_pins=(board.P1_00, board.P0_11, board.P1_04, board.P1_06),
#    interval=0.050,
#)
MODE_KEY = (
    board.P1_15,
)

# define key matrix
cols = [DigitalInOut(x) for x in (board.P1_00, board.P0_11, board.P1_04, board.P1_06)]
rows = [DigitalInOut(x) for x in (board.P0_22, board.P0_24, board.P0_31)]
keys = ((1, 2, 3, 4),
        (5, 6, 7, 8),
        (9, 10, 11, 12))

mode = keypad.Keys((board.P1_15,), value_when_pressed=False, pull=True)

#encoder = rotaryio.IncrementalEncoder(board.P1_11, board.P1_13) # left encoder
encoder = rotaryio.IncrementalEncoder(board.P0_09, board.P0_10) # right encoder
last_position = None

keypad = adafruit_matrixkeypad.Matrix_Keypad(rows, cols, keys)

def checkModeButton():
    event = mode.events.get()
    # event will be None if nothing has happened.
    if event:
        print(event)# Write

while True:
    checkModeButton()
    keys = keypad.pressed_keys
    for key in keys:
        if key == 1:
            keyboard.send(Keycode.CONTROL, Keycode.SHIFT, Keycode.S) # save replay
        elif key == 2:
            keyboard.send(Keycode.F1) # emote in apex
        elif key == 3:
            keyboard.send(Keycode.PRINT_SCREEN) # screenshot
        elif key == 4:
            keyboard.send(Keycode.CONTROL, Keycode.L) # leave webex
        elif key == 5:
            layout.write("Pack my box with five dozen liquor jugs.")
        elif key == 6:
            layout.write("Pack my box with five dozen liquor jugs.")
        elif key == 8:
            layout.write("Pack my box with five dozen liquor jugs.")
        elif key == 9:
            layout.write("Pack my box with five dozen liquor jugs.")
        elif key == 10:
            layout.write("Pack my box with five dozen liquor jugs.")
        elif key == 11:
            layout.write("Pack my box with five dozen liquor jugs.")
        elif key == 12:
            keyboard.send(Keycode.CONTROL, Keycode.ALT, Keycode.DELETE) # bring up task manager
    if keys:
        print("Pressed: ", keys)
    time.sleep(0.1)


