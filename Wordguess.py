import random
import time
import os


def clear():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')
# List of words to choose from
words = ["apple", "banana", "orange", "grape", "strawberry", "pineapple"]

# Function to choose a random word from the list
def choose_word():
    return random.choice(words)

# Function to play the game
def play_game():
    word = choose_word()
    guessed_letters = []
    attempts = 6

    print("Welcome to Word Guess!")
    print("The word contains", len(word), "letters.")
    print("You have", attempts, "attempts remaining.")

    while attempts > 0:
        # Display the word with correctly guessed letters
        display_word = ""
        for letter in word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "
        print(display_word)

        # Prompt the player to guess a letter
        guess = input("Guess a letter: ").lower()

        # Check if the guessed letter is correct
        if guess in word:
            if guess not in guessed_letters:
                guessed_letters.append(guess)
                print("Correct!")
                clear()
            else:
                print("You've already guessed that letter.")
                ()
        else:
            print("Wrong guess!")
            attempts -= 1
            clear()
            print("You have", attempts, "attempts remaining.")

        # Check if the player has won or lost
        if set(guessed_letters) == set(word):
            print("Congratulations! You guessed the word:", word)
            time.sleep(3)
            clear()
            import Singleplayergames
            break
        elif attempts == 0:
            print("Game over! The word was:", word)
            time.sleep(3)
            clear()
            import Singleplayergames
            break

# Start the game
play_game()
