import random
import time
import os

def clear():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')
def simon_says():
    print("Welcome to Simon Says!")
    print("Watch the pattern and repeat it.")
    time.sleep(2)

    pattern = []
    player_input = []
    game_over = False

    while not game_over:
        # Add a random number (1-4) to the pattern
        number = random.randint(1, 4)
        pattern.append(number)

        # Display the pattern to the player
        for num in pattern:
            print("Simon says:", num)
            time.sleep(1)
            print("")

        # Clear the screen
        time.sleep(2)
        print("\n" * 50)

        # Player's turn to repeat the pattern
        print("Your turn to repeat the pattern!")
        for _ in range(len(pattern)):
            guess = int(input("Enter the number: "))
            player_input.append(guess)

        # Check if the player's input matches the pattern
        for i in range(len(pattern)):
            if pattern[i] != player_input[i]:
                game_over = True
                break

        if game_over:
            print("Game over! You made a mistake.")
            time.sleep(3)
            clear()
            import Singleplayergames
        else:
            print("Good job! You repeated the pattern correctly.")
            time.sleep(3)
            clear()
            import Singleplayergames

simon_says()
