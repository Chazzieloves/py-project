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


def is_winner(revealed):
    """Check if player won."""
    for line in revealed:
        if False in line:
            return False
    return True


# Main function.


def main():
    """Main loop."""
    revealed = [[False] * GRID_SIZE for _ in range(GRID_SIZE)]
    attempts = 0
    score = 0

    while not is_winner(revealed):
        display_board(BOARD, revealed)
        print(f"Attempts: {attempts} Score: {score}")

        # Get input from user on first card.
        while True:
            try:
                row1, col1 = map(int, input("Enter row and column: ").split())
                if (
                    0 <= row1 < GRID_SIZE
                    and 0 <= col1 < GRID_SIZE
                    and not revealed[row1][col1]
                ):
                    break
                else:
                    print("Try again.")
            except ValueError:
                print("Try again.")

        # Get input from user on second card.
        while True:
            try:
                row2, col2 = map(int, input("Enter row and column: ").split())
                if (
                    0 <= row2 < GRID_SIZE
                    and 0 <= col2 < GRID_SIZE
                    and (row1 != row2 or col1 != col2)
                    and not revealed[row2][col2]
                ):
                    break
                else:
                    print("Invalid input, try again.")
            except ValueError:
                print("Invalid input, try again.")

        # Reveal selected cards.
        tries += 1
        if BOARD[row1][col1] == BOARD[row2][col2]:
            print("It´s a match!")
            revealed[row1][col1] = revealed[row2][col2] = True
            score += 1
        else:
            print("Not a match. Try again!")

    print("Yeeey! You won!")
    print(f"Total Tries: {tries} Total Score: {score}")

    if __name__ == "__main__":
        main()
