"""Create memory game"""

import random

GRID_SIZE = 4
SYMBOLS = "ABCDEFGHIJKLMNOPQRST"
CARDS = random.sample(SYMBOLS, GRID_SIZE * GRID_SIZE // 2) * 2
random.shuffle(CARDS)
board = [[None] * GRID_SIZE for _ in range(GRID_SIZE)]

for row in range(GRID_SIZE):
    for col in range(GRID_SIZE):
        board[row][col] = CARDS.pop()
