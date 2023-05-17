import time
import os

def clear():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')
def game_menu():
    print("Welcome to the Game Menu!")
    print("1. Singleplayer Games")
    print("2. Multiplayer Games")
    print("3. Exit")
    print()

    choice = input("Enter the number corresponding to your choice: ")

    if choice == "1":
        print("Opening Singleplayer games...")
        time.sleep(3)
        clear()
        import Singleplayergames
        # Call the function to start the Tic Tac Toe game
        # tic_tac_toe()
    elif choice == "2":
        print("Opening Multiplayer Games...")
        time.sleep(3)
        clear()
        import Multiplayergames
        # Call the function to start the Hangman game
        # hangman()
    elif choice == "3":
        print("Exiting the program...")
        time.sleep(3)
        exit()
    else:
        print("Invalid choice. Please try again.")

game_menu()
