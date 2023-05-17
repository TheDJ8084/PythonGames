import time
import os

def clear():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')
def game_menu():
    print("Multiplayer Games")
    print("1. Tic Tac Toe")
    print("2. Main Menu")
    print()

    choice = input("Enter the number corresponding to your choice: ")

    if choice == "1":
        print("Starting Tic Tac Toe...")
        time.sleep(3)
        clear()
        import Tictactoe
        # Call the function to start the Tic Tac Toe game
        # tic_tac_toe()
    elif choice == "2":
        print("Going back to the main menu...")
        time.sleep(3)
        clear()
        import Mainmenu
        # Call the function to start the Guess the Number game
        # guess_the_number()
    else:
        print("Invalid choice. Please try again.")

game_menu()
