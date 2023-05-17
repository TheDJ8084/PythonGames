import os
import time

def clear():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return row[0]

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]

    return None

def tic_tac_toe():
    print("Welcome to Tic Tac Toe!")
    print("Player 1: X")
    print("Player 2: O")
    print("Let's begin!")
    print()

    board = [[" " for _ in range(3)] for _ in range(3)]
    player = 1

    while True:
        print_board(board)
        print()

        if player == 1:
            symbol = "X"
        else:
            symbol = "O"

        row = int(input("Player {} - Enter the row (0-2): ".format(player)))
        col = int(input("Player {} - Enter the column (0-2): ".format(player)))
        clear()
        print()

        if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == " ":
            board[row][col] = symbol
            winner = check_winner(board)

            if winner:
                print_board(board)
                print("Congratulations! Player {} wins!".format(player))
                time.sleep(3)
                clear()
                import Multiplayergames
                break

            if all(all(cell != " " for cell in row) for row in board):
                print_board(board)
                print("It's a tie!")
                time.sleep(3)
                clear()
                import Multiplayergames
                break

            player = 3 - player  # Switch players (1 -> 2, 2 -> 1)
        else:
            print("Invalid move. Try again.")
            print()

tic_tac_toe()
