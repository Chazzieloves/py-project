"""Create memory game."""

import random

GRID_SIZE = 4
SYMBOLS = "ABCDEFGHIJKLMNOPQRST"
CARDS = random.sample(SYMBOLS, GRID_SIZE * GRID_SIZE // 2) * 2
random.shuffle(CARDS)
BOARD = [[None] * GRID_SIZE for _ in range(GRID_SIZE)]

for row in range(GRID_SIZE):
    for col in range(GRID_SIZE):
        BOARD[row][col] = CARDS.pop()

# Display cards on board. They are hidden from start.


def display_board(board, revealed):
    """Display board."""
    for line in range(GRID_SIZE):
        for card in range(GRID_SIZE):
            if not revealed[line][card]:
                print(board[line][card], end=" ")
            else:
                print("?", end=" ")
        print()
