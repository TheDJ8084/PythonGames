import pygame
import random

def clear():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')

# Initialize Pygame
pygame.init()

# Set the dimensions of the window
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Pong Game")

# Set colors
background_color = (0, 0, 0)
paddle_color = (255, 255, 255)
ball_color = (255, 255, 255)

# Set paddles' dimensions and movement speed
paddle_width = 10
paddle_height = 80
paddle_speed = 5

# Set the ball's dimensions and movement speed
ball_radius = 10
ball_speed_x = 3
ball_speed_y = 3

# Set the initial positions of the paddles and the ball
left_paddle_x = 50
left_paddle_y = window_height // 2 - paddle_height // 2
right_paddle_x = window_width - 50 - paddle_width
right_paddle_y = window_height // 2 - paddle_height // 2
ball_x = window_width // 2
ball_y = window_height // 2

# Set the initial directions of the ball
ball_direction_x = random.choice([-1, 1])
ball_direction_y = random.choice([-1, 1])

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the window
    window.fill(background_color)

    # Move the paddles
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        if left_paddle_y > 0:
            left_paddle_y -= paddle_speed
    if keys[pygame.K_DOWN]:
        if left_paddle_y < window_height - paddle_height:
            left_paddle_y += paddle_speed
    if keys[pygame.K_w]:
        if right_paddle_y > 0:
            right_paddle_y -= paddle_speed
    if keys[pygame.K_s]:
        if right_paddle_y < window_height - paddle_height:
            right_paddle_y += paddle_speed

    # Update the ball's position
    ball_x += ball_speed_x * ball_direction_x
    ball_y += ball_speed_y * ball_direction_y

    # Detect collisions with the paddles
    if ball_x <= left_paddle_x + paddle_width and left_paddle_y <= ball_y <= left_paddle_y + paddle_height:
        ball_direction_x = 1
    if ball_x >= right_paddle_x - ball_radius and right_paddle_y <= ball_y <= right_paddle_y + paddle_height:
        ball_direction_x = -1

    # Detect collisions with the top and bottom walls
    if ball_y <= 0 or ball_y >= window_height - ball_radius:
        ball_direction_y *= -1

    # Draw the paddles
    pygame.draw.rect(window, paddle_color, (left_paddle_x, left_paddle_y, paddle_width, paddle_height))
    pygame.draw.rect(window, paddle_color, (right_paddle_x, right_paddle_y, paddle_width, paddle_height))

    # Draw the ball
    pygame.draw.circle(window, ball_color, (ball_x, ball_y), ball_radius)

    # Update the display
    pygame.display.update()

# Quit the game
clear()
import Multiplayergames
pygame.quit()
