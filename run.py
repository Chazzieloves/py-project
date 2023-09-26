"""Create memory game."""
import os
import random
from time import sleep

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


def display_board_preview(board, revealed):
    """Display board."""
    for line in range(GRID_SIZE):
        for card in range(GRID_SIZE):
            if revealed[line][card]:
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
    game_start = True
    revealed = [[False] * GRID_SIZE for _ in range(GRID_SIZE)]
    attempts = 0
    score = 0

    while not is_winner(revealed):
        os.system("cls" if os.name == "nt" else "clear")
        if game_start:
            print(
                "Test your memory!"
                " ----- RULES -----"
                "Try to find the pair of letters underneath the '?'"
                "To choose two cards, enter the row and column number like this '1 2, 0 3'."
                "The first number you add represents row and the next column."
                "The comma sparates the selected cards."
                "You can only reveal two cards at a time."
                "If they match, you get a point!"
                "If they do not, try again!"
                "The game end when you find all the pairs."
                "Good luck!"
                " -----------------"
            )
            game_start = False
        print(revealed)
        display_board_preview(BOARD, revealed)
        sleep(2)
        os.system("cls" if os.name == "nt" else "clear")
        display_board(BOARD, revealed)
        # if False * GRID_SIZE in revealed:
        # if True show a letter.
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
                row2, col2 = map(
                    int,
                    input("Enter row and column in following format: '1 3' ").split(),
                )
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
        attempts += 1
        if BOARD[row1][col1] == BOARD[row2][col2]:
            print("It´s a match!")
            sleep(2)
            revealed[row1][col1] = revealed[row2][col2] = True
            score += 1
        else:
            print("Not a match. Try again!")
            sleep(2)

    print("Yeeey! You won!")
    print(f"Total Attempts: {attempts} Total Score: {score}")


if __name__ == "__main__":
    main()
