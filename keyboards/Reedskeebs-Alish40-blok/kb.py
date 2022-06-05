import board
from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners import DiodeOrientation

class KMKKeyboard(_KMKKeyboard):
    col_pins = (board.D0, board.D1, board.D2, board.D3, board.D4, board.D5, board.D10, board.MOSI, board.D9, board.D8, board.D7, board.D6)
    row_pins = (board.A1, board.A0, board.SCK, board.MISO)
    diode_orientation = DiodeOrientation.COL2ROW
