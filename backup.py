import board
import keypad
import usb_hid

print("Hello World")

KEY_PINS = (
    board.P0_06,
    board.P0_08,
    board.P0_17,
    board.P0_20,
    board.P0_22,
    board.P0_24,
    board.P1_00,
    board.P0_11,
    board.P1_04,
    board.P1_06,
    board.P0_31,
    board.P0_29,
    board.P1_15,
    board.P1_13,
    board.P1_11,
    board.P0_10,
    board.P0_09,
    )

# keys = keypad.Keys((board.P0_24,), value_when_pressed=False, pull=True)
# keys = keypad.Keys((board.D5,), value_when_pressed=False, pull=True)
keys = keypad.Keys(KEY_PINS, value_when_pressed=False, pull=True)


while True:
    event = keys.events.get()
    # event will be None if nothing has happened.
    if event:
        print(event)# Write your code here :-)
