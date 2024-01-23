# Import random package to be able to create random integers
import random


# The Game Board
def print_board(board):
    for row in board:
        print(" ".join(row))


def random_row(board):
    return random.randint(0, len(board) - 1)


def random_col(board):
    return random.randint(0, len(board[0]) - 1)


# User input
def get_user_input(prompt):
    try:
        return int(input(prompt))
    except ValueError:
        print("Please enter a number.")
        return get_user_input(prompt)


# Main code for the game board
def main():
    board_size = 5
    board = [["O"] * board_size for _ in range(board_size)]

    ship_row = random_row(board)
    ship_col = random_col(board)

    print("Welcome to my Battleship Game - Good Luck!")
    print_board(board)

