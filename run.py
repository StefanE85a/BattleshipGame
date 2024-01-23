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
