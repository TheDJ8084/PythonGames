import pygame
import random
import sys
import subprocess

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600
WINDOW_SIZE = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Blackjack")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 128, 0)
RED = (255, 0, 0)

# Fonts
FONT_LARGE = pygame.font.Font(None, 48)
FONT_MEDIUM = pygame.font.Font(None, 36)
FONT_SMALL = pygame.font.Font(None, 24)

# Game variables
deck = [
    2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,
    2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,
    2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,
    2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11
]
random.shuffle(deck)

player_cards = []
dealer_cards = []

def open_new_file():
    subprocess.Popen([sys.executable, 'Singleplayergames.py'])
    pygame.quit()
    sys.exit()

def draw_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x, y)
    screen.blit(text_surface, text_rect)

def draw_card(card, x, y):
    card_image = pygame.image.load(f"cards/{card}.png")
    screen.blit(card_image, (x, y))

# Game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_h:
                # Player chooses to Hit
                player_cards.append(deck.pop())
            elif event.key == pygame.K_s:
                # Player chooses to Stand
                while sum(dealer_cards) < 17:
                    dealer_cards.append(deck.pop())

    # Game logic
    if len(player_cards) == 0 and len(dealer_cards) == 0:
        # Deal initial cards
        for _ in range(2):
            player_cards.append(deck.pop())
            dealer_cards.append(deck.pop())

        # Check if player or dealer has blackjack
        player_sum = sum(player_cards)
        dealer_sum = sum(dealer_cards)

        if player_sum == 21 or dealer_sum == 21:
            # Game over
            open_new_file()

    # Drawing
    screen.fill(WHITE)

    # Draw player's cards
    draw_text("Your Cards:", FONT_LARGE, BLACK, 10, 10)

    x_pos = 10
    for card in player_cards:
        draw_card(card, x_pos, 60)
        x_pos += 80

    # Draw dealer's cards
    draw_text("Dealer's Cards:", FONT_LARGE, BLACK, 10, 250)

    x_pos = 10
    for card in dealer_cards:
        draw_card(card, x_pos, 290)
        x_pos += 80

    # Draw instructions
    draw_text("BLACKJACK", FONT_LARGE, BLACK, 280, 10)
    draw_text("Press 'H' to Hit", FONT_MEDIUM, GREEN, 280, 100)
    draw_text("Press 'S' to Stand", FONT_MEDIUM, RED, 280, 150)

    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
