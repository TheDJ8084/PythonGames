import time
import os

def clear():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')
def game_menu():
    print("Singleplayer Games")
    print("1. Hangman")
    print("2. Guess the Number")
    print("3. Simon Says")
    print("4. Word Guess")
    print("5. Main Menu")
    print()

    choice = input("Enter the number corresponding to your choice: ")

    if choice == "1":
        print("Starting Hangman...")
        time.sleep(3)
        clear()
        import Tictactoe
        # Call the function to start the Tic Tac Toe game
        # tic_tac_toe()
    elif choice == "2":
        print("Starting Guess the Number...")
        time.sleep(3)
        clear()
        import Hangman
        # Call the function to start the Hangman game
        # hangman()
    elif choice == "3":
        print("Starting Simon Says...")
        time.sleep(3)
        clear()
        import Simonsays
    elif choice == "4":
        print("Starting Word Guess...")
        time.sleep(3)
        clear()
        import Wordguess
    elif choice == "5":
        print("Going back to the main menu...")
        time.sleep(3)
        clear()
        import Mainmenu
        # Call the function to start the Guess the Number game
        # guess_the_number()
    else:
        print("Invalid choice. Please try again.")

game_menu()
