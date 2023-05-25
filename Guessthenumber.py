import pygame
import random
import subprocess

# Initialize Pygame
pygame.init()

# Set up the game window
window_width = 400
window_height = 500
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Guess the Number")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Load fonts
title_font = pygame.font.Font(None, 48)
text_font = pygame.font.Font(None, 28)

# Game variables
secret_number = random.randint(1, 100)
guesses_taken = 0
max_guesses = 10

# Function to open another Python file and close the current window
def open_file(file_path):
    subprocess.Popen(['python', file_path])
    pygame.quit()
    quit()

# Function to display text on the screen
def draw_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    window.blit(text_surface, text_rect)

# Game loop
running = True
number_input = ""
result_text = ""  # Initialize the result_text variable
result_color = BLACK
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                # Check the guessed number
                if number_input != "":
                    guess = int(number_input)
                    guesses_taken += 1

                    if guess < secret_number:
                        result_text = "Too low!"
                        result_color = RED
                    elif guess > secret_number:
                        result_text = "Too high!"
                        result_color = RED
                    else:
                        result_text = "Congratulations! You guessed it!"
                        result_color = GREEN
                        pygame.time.wait(2000)
                        open_file("Singleplayergames.py")
                        running = False
                        break

                    if guesses_taken >= max_guesses:
                        result_text = "Game over! The number was " + str(secret_number)
                        result_color = RED
                        pygame.time.wait(2000)
                        open_file("Singleplayergames.py")
                        running = False
                        break

                    number_input = ""

                else:
                    result_text = "Please enter a number!"
                    result_color = RED

            elif event.key == pygame.K_BACKSPACE:
                number_input = number_input[:-1]

            else:
                number_input += event.unicode

    # Clear the screen
    window.fill(WHITE)

    # Draw title
    draw_text("Guess the Number", title_font, BLACK, window_width // 2, 50)

    # Draw instructions
    draw_text("Guess the number (1-100):", text_font, BLACK, window_width // 2, 150)

    # Draw number of guesses
    draw_text("Guesses taken: " + str(guesses_taken), text_font, BLACK, window_width // 2, 200)

    # Draw input box
    pygame.draw.rect(window, BLACK, (50, 250, 300, 40))
    pygame.draw.rect(window, WHITE, (53, 253, 294, 34))

    # Draw current guess
    draw_text(number_input, text_font, BLACK, window_width // 2, 275)

    # Draw result
    draw_text(result_text, text_font, result_color, window_width // 2, 350)

    pygame.display.flip()

# Quit Pygame
pygame.quit()
