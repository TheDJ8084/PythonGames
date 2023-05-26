import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the game window
window_width = 800
window_height = 400
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Multiplayer Pong Game")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Paddle constants
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 60
PADDLE_SPEED = 5

# Ball constants
BALL_WIDTH = 10
BALL_HEIGHT = 10
BALL_SPEED_X = 3
BALL_SPEED_Y = 3

# Score variables
player1_score = 0
player2_score = 0
font = pygame.font.Font(None, 36)

# Create the paddles
player1_paddle = pygame.Rect(50, window_height // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
player2_paddle = pygame.Rect(window_width - 50 - PADDLE_WIDTH, window_height // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)

# Create the ball
ball = pygame.Rect(window_width // 2 - BALL_WIDTH // 2, window_height // 2 - BALL_HEIGHT // 2, BALL_WIDTH, BALL_HEIGHT)
ball_speed_x = BALL_SPEED_X
ball_speed_y = BALL_SPEED_Y

# Main game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the paddles
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player1_paddle.top > 0:
        player1_paddle.y -= PADDLE_SPEED
    if keys[pygame.K_s] and player1_paddle.bottom < window_height:
        player1_paddle.y += PADDLE_SPEED
    if keys[pygame.K_UP] and player2_paddle.top > 0:
        player2_paddle.y -= PADDLE_SPEED
    if keys[pygame.K_DOWN] and player2_paddle.bottom < window_height:
        player2_paddle.y += PADDLE_SPEED

    # Move the ball
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Collision detection with paddles
    if ball.colliderect(player1_paddle) or ball.colliderect(player2_paddle):
        ball_speed_x *= -1

    # Collision detection with walls
    if ball.top < 0 or ball.bottom > window_height:
        ball_speed_y *= -1

    # Scoring
    if ball.left < 0:
        player2_score += 1
        if player2_score == 10:
            print("Player 2 wins!")
            running = False
    elif ball.right > window_width:
        player1_score += 1
        if player1_score == 10:
            print("Player 1 wins!")
            running = False

    # Draw the game elements
    window.fill(BLACK)
    pygame.draw.rect(window, WHITE, player1_paddle)
    pygame.draw.rect(window, WHITE, player2_paddle)
    pygame.draw.ellipse(window, WHITE, ball)
    pygame.draw.aaline(window, WHITE, (window_width // 2, 0), (window_width // 2, window_height))

    # Render the scores
    player1_text = font.render(str(player1_score), True, WHITE)
    player2_text = font.render(str(player2_score), True, WHITE)
    window.blit(player1_text, (window_width // 2 - 50, 10))
    window.blit(player2_text, (window_width // 2 + 30, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
