import random
import time
import os

def clear():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')

# List of words to choose from
words = ["Toyota", "Ford", "Chevrolet", "Honda", "Nissan", "Jeep", "Hyundai", "Kia", "RAM", "Subaru", "GMC", "Volkswagen", "BMW", "Mazda", "Mercedes", "Lexus", "Tesla", "Dodge", "Audi", "Buick", "Acura", "Volvo", "Cadillac", "Chrysler", "Mitsubishi", "Porsche", "Lincoln", "Infiniti", "Genesis", "Mini", "Maserati", "Jaguar", "Bentley","Ferrari","Lamborghini","Polestar","Fiat","Mclaren","Lucid","Bugatti","Lotus","Rivian","Pontiac","Oldsmobile","Rimac"]

# Function to choose a random word from the list
def choose_word():
    return random.choice(words)

# Function to play the game
def play_game():
    word = choose_word()
    guessed_word = ""
    attempts = 10

    print("Welcome to Word Guess!")
    print("The word contains", len(word), "letters and is a car brand")
    print("You have", attempts, "attempts remaining.")

    while attempts > 0:
        # Display the word with correctly guessed letters
        display_word = ""
        for letter in word:
            if letter in guessed_word:
                display_word += letter + " "
            else:
                display_word += "_ "
        print(display_word)

        # Prompt the player to guess a letter or the whole word
        guess = input("Guess a letter or the whole word: ").lower()

        # Check if the guess is a letter or the whole word
        if len(guess) == 1:
            # Guess is a letter
            if guess in word:
                if guess not in guessed_word:
                    guessed_word += guess
                    print("Correct!")
                    clear()
                else:
                    print("You've already guessed that letter.")
            else:
                print("Wrong guess!")
                attempts -= 1
                clear()
                print("You have", attempts, "attempts remaining.")
        else:
            # Guess is the whole word
            if guess == word:
                print("Congratulations! You guessed the word:", word)
                time.sleep(3)
                clear()
                import Singleplayergames
                break
            else:
                print("Wrong guess!")
                attempts -= 1
                clear()
                print("You have", attempts, "attempts remaining.")

        # Check if the player has won or lost
        if set(guessed_word) == set(word):
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
