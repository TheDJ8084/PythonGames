import random
import time
import os

def clear():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')
def hangman():
    word_list = ["apple", "banana", "cherry", "durian", "elderberry", "fig", "grape", "honeydew", "jackfruit", "kiwi"]
    chosen_word = random.choice(word_list).lower()
    guessed_letters = []
    max_guesses = 6
    incorrect_guesses = 0

    print("Welcome to Hangman!")
    print("Try to guess the word.")

    while True:
        # Display current progress
        masked_word = ""
        for letter in chosen_word:
            if letter in guessed_letters:
                masked_word += letter + " "
            else:
                masked_word += "_ "
        print(masked_word)

        # Prompt the player for a letter
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        guessed_letters.append(guess)

        if guess in chosen_word:
            print("Correct guess!")
        else:
            incorrect_guesses += 1
            print("Incorrect guess.")

        # Check if the player has won or lost
        if all(letter in guessed_letters for letter in chosen_word):
            print("Congratulations! You guessed the word: " + chosen_word)
            time.sleep(3)
            clear()
            import Singleplayergames
            break

        if incorrect_guesses == max_guesses:
            print("You lost! The word was: " + chosen_word)
            time.sleep(3)
            clear()
            import Singleplayergames
            break

        print("Remaining guesses:", max_guesses - incorrect_guesses)
        print()

hangman()
