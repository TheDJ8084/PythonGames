import random
import pygame
import os
import time
import subprocess

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH = 800
HEIGHT = 600
FPS = 60
FONT_SIZE = 40

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Word Guess")
clock = pygame.time.Clock()

# Function to clear the console or terminal
def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

# List of words to choose from
words = [
    "Toyota", "Ford", "Chevrolet", "Honda", "Nissan", "Jeep", "Hyundai", "Kia",
    "RAM", "Subaru", "GMC", "Volkswagen", "BMW", "Mazda", "Mercedes", "Lexus",
    "Tesla", "Dodge", "Audi", "Buick", "Acura", "Volvo", "Cadillac", "Chrysler",
    "Mitsubishi", "Porsche", "Lincoln", "Infiniti", "Genesis", "Mini", "Maserati",
    "Jaguar", "Bentley", "Ferrari", "Lamborghini", "Polestar", "Fiat", "Mclaren",
    "Lucid", "Bugatti", "Lotus", "Rivian", "Pontiac", "Oldsmobile", "Rimac"
]

# Function to choose a random word from the list
def choose_word():
    return random.choice(words)

# Function to draw text on the screen
def draw_text(surface, text, font_size, x, y):
    font = pygame.font.Font(None, font_size)
    text_surface = font.render(text, True, BLACK)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    surface.blit(text_surface, text_rect)

# Function to play the game
def play_game():
    word = choose_word()
    guessed_word = ""
    attempts = 10

    running = True
    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(WHITE)

        # Display the word with correctly guessed letters
        display_word = ""
        for letter in word:
            if letter in guessed_word:
                display_word += letter + " "
            else:
                display_word += "_ "
        draw_text(screen, display_word, FONT_SIZE, WIDTH / 2, HEIGHT / 2 - FONT_SIZE)

        # Draw attempts remaining
        draw_text(screen, "Attempts: " + str(attempts), FONT_SIZE, WIDTH / 2, HEIGHT / 2)

        # Prompt the player to guess a letter or the whole word
        draw_text(screen, "Guess a letter or the whole word", FONT_SIZE, WIDTH / 2, HEIGHT / 2 + FONT_SIZE)

        pygame.display.flip()

        # Check if the player has won or lost
        if set(guessed_word) == set(word):
            draw_text(screen, "Congratulations! You guessed the word: " + word, FONT_SIZE, WIDTH / 2, HEIGHT / 2)
            pygame.display.flip()
            time.sleep(3)
            subprocess.call(["python", "WordGuessMenu.py"])  # Replace "win_script.py" with the filename of the script you want to run on win
            break
        elif attempts == 0:
            draw_text(screen, "Game over! The word was: " + word, FONT_SIZE, WIDTH / 2, HEIGHT / 2)
            pygame.display.flip()
            time.sleep(3)
            subprocess.call(["python", "WordGuessMenu.py"])  # Replace "lose_script.py" with the filename of the script you want to run on loss
            break

        # Check for player input
        keys = pygame.key.get_pressed()
        for key in keys:
            if keys[pygame.K_a] and "a" not in guessed_word:
                guess = "a"
            elif keys[pygame.K_b] and "b" not in guessed_word:
                guess = "b"
            # Add other letters as needed

        # Check if the guess is correct
        if guess in word:
            if guess not in guessed_word:
                guessed_word += guess
                clear()
                print("Correct!")
            else:
                print("You've already guessed that letter.")
        else:
            print("Wrong guess!")
            attempts -= 1
            clear()
            print("You have", attempts, "attempts remaining.")

    pygame.quit()

# Start the game
play_game()
