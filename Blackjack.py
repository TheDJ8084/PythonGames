import pygame
import random
import subprocess
import sys

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

# Game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

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
    player_text = pygame.font.Font(None, 36).render("Player Cards:", True, BLACK)
    screen.blit(player_text, (10, 10))

    x_pos = 10
    for card in player_cards:
        card_text = pygame.font.Font(None, 36).render(str(card), True, BLACK)
        screen.blit(card_text, (x_pos, 50))
        x_pos += 40

    # Draw dealer's cards
    dealer_text = pygame.font.Font(None, 36).render("Dealer Cards:", True, BLACK)
    screen.blit(dealer_text, (10, 150))

    x_pos = 10
    for card in dealer_cards:
        card_text = pygame.font.Font(None, 36).render(str(card), True, BLACK)
        screen.blit(card_text, (x_pos, 190))
        x_pos += 40

    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
