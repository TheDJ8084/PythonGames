import random
import time
import os

def clear():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')
def guess_the_number():
    print("Welcome to Guess the Number!")
    print("I'm thinking of a number between 1 and 100.")
    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        guess = int(input("Take a guess: "))
        attempts += 1

        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        else:
            print("Congratulations! You guessed the number in", attempts, "attempts!")
            time.sleep(3)
            clear()
            import Singleplayergames
            break

guess_the_number()
