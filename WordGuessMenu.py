import pygame
import os
import sys

# Initialize Pygame and set up the window
pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Word Guess")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Flag to indicate if the game should be ended
end_game = False


def execute_file(file_name):
    global end_game
    end_game = True
    pygame.quit()
    os.system("python " + file_name)


def button_clicked1():
    execute_file("Wordguessfruits.py")


def button_clicked2():
    execute_file("Wordguesscarbrands.py")


def button_clicked3():
    execute_file("Singleplayergames.py")


class Button:
    def __init__(self, text, x, y, width, height, action):
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)
        self.action = action

    def draw(self):
        pygame.draw.rect(screen, WHITE, self.rect)
        font = pygame.font.Font(None, 30)
        text = font.render(self.text, True, BLACK)
        text_rect = text.get_rect(center=self.rect.center)
        screen.blit(text, text_rect)

    def clicked(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.action()


# Calculate the x-coordinate for the centered buttons
button_width = 200
button_x = (screen.get_width() - button_width) // 2

button1 = Button("Fruits", button_x, 200, button_width, 50, button_clicked1)
button2 = Button("Car Brands", button_x, 300, button_width, 50, button_clicked2)
button3 = Button("Back to Menu", button_x, 400, button_width, 50, button_clicked3)

title_font = pygame.font.Font(None, 40)
title_text = title_font.render("Word Guess", True, WHITE)
title_text_rect = title_text.get_rect(center=(screen.get_width() // 2, 100))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()  # Close the Python script
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                button1.clicked()
                button2.clicked()
                button3.clicked()

    screen.fill(BLACK)
    screen.blit(title_text, title_text_rect)
    button1.draw()
    button2.draw()
    button3.draw()
    pygame.display.flip()

    if end_game:
        break

pygame.quit()
