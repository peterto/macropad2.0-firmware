import keypad
import board
import rotaryio
#from adafruit_macropad import MacroPad
import adafruit_matrixkeypad
from digitalio import DigitalInOut

#macropad = MacroPad()

km = keypad.KeyMatrix(
    row_pins=(board.P0_22, board.P0_24, board.P0_31),
    column_pins=(board.P1_00, board.P0_11, board.P1_04, board.P1_06),
    interval=0.050,
)

#encoder = rotaryio.IncrementalEncoder(board.P1_11, board.P1_13) # left encoder
encoder = rotaryio.IncrementalEncoder(board.P0_09, board.P0_10) # right encoder
last_position = None


while True:
    event = km.events.get()
    if event:
        print(event)

    position = encoder.position
    if last_position is None or position != last_position:
        print(position)
    last_position = position
