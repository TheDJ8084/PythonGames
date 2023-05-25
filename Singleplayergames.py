import pygame
import os
import sys

# Initialize Pygame and set up the window
pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Singleplayer Games")

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
    execute_file("Mazegame.py")


def button_clicked2():
    execute_file("Guessthenumber.py")


def button_clicked3():
    execute_file("Simonsays.py")


def button_clicked4():
    execute_file("WordGuessMenu.py")


def button_clicked5():
    execute_file("Snake.py")


def button_clicked6():
    execute_file("Blackjack.py")


def button_clicked7():
    execute_file("Mainmenu.py")


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

button1 = Button("Maze Game", button_x, 150, button_width, 50, button_clicked1)
button2 = Button("Guess the Number", button_x, 250, button_width, 50, button_clicked2)
button3 = Button("Simon Says", button_x, 350, button_width, 50, button_clicked3)
button4 = Button("Word Guess", button_x, 450, button_width, 50, button_clicked4)
button5 = Button("Snake", button_x, 550, button_width, 50, button_clicked5)
button6 = Button("Blackjack", button_x, 650, button_width, 50, button_clicked6)
button7 = Button("Back to Main Menu", button_x, 750, button_width, 50, button_clicked7)

title_font = pygame.font.Font(None, 40)
title_text = title_font.render("Singleplayer Games", True, WHITE)
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
                button4.clicked()
                button5.clicked()
                button6.clicked()
                button7.clicked()

    screen.fill(BLACK)
    screen.blit(title_text, title_text_rect)
    button1.draw()
    button2.draw()
    button3.draw()
    button4.draw()
    button5.draw()
    button6.draw()
    button7.draw()
    pygame.display.flip()

    if end_game:
        break

pygame.quit()
