import pygame
import random
import os

# Initialize Pygame and set up the window
pygame.init()
screen_width, screen_height = 640, 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game")

# Define colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Define the snake and food sizes
snake_size = 20
food_size = 20

# Define the snake's movement speed
snake_speed = 10

clock = pygame.time.Clock()


def game_over():
    # Code to execute when the game is over
    # For example, you can call another Python file here
    os.system("Singleplayergames.py")
    pygame.quit()


def draw_snake(snake_body):
    for block in snake_body:
        pygame.draw.rect(screen, GREEN, [block[0], block[1], snake_size, snake_size])


def draw_food(food_position):
    pygame.draw.rect(screen, RED, [food_position[0], food_position[1], food_size, food_size])


def run_game():
    # Set up initial snake and food positions
    snake_body = [[screen_width / 2, screen_height / 2]]
    food_position = [random.randint(1, (screen_width - food_size) // food_size) * food_size,
                     random.randint(1, (screen_height - food_size) // food_size) * food_size]

    # Set up initial movement direction
    direction = "RIGHT"

    game_over_flag = False

    while not game_over_flag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != "DOWN":
                    direction = "UP"
                elif event.key == pygame.K_DOWN and direction != "UP":
                    direction = "DOWN"
                elif event.key == pygame.K_LEFT and direction != "RIGHT":
                    direction = "LEFT"
                elif event.key == pygame.K_RIGHT and direction != "LEFT":
                    direction = "RIGHT"

        # Update snake position based on the direction
        if direction == "UP":
            snake_body[0][1] -= snake_speed
        elif direction == "DOWN":
            snake_body[0][1] += snake_speed
        elif direction == "LEFT":
            snake_body[0][0] -= snake_speed
        elif direction == "RIGHT":
            snake_body[0][0] += snake_speed

        # Check if the snake has hit the boundaries
        if snake_body[0][0] >= screen_width or snake_body[0][0] < 0 or snake_body[0][1] >= screen_height or snake_body[0][1] < 0:
            game_over_flag = True

        # Check if the snake has hit itself
        for block in snake_body[1:]:
            if snake_body[0][0] == block[0] and snake_body[0][1] == block[1]:
                game_over_flag = True

        # Check if the snake has eaten the food
        if snake_body[0][0] == food_position[0] and snake_body[0][1] == food_position[1]:
            # Generate new food position
            food_position = [random.randint(1, (screen_width - food_size) // food_size) * food_size,
                             random.randint(1, (screen_height - food_size) // food_size) * food_size]

            # Extend the length of the snake
            new_block = list(snake_body[-1])
            if direction == "UP":
                new_block[1] += snake_size
            elif direction == "DOWN":
                new_block[1] -= snake_size
            elif direction == "LEFT":
                new_block[0] += snake_size
            elif direction == "RIGHT":
                new_block[0] -= snake_size

            snake_body.append(new_block)

        # Update the game screen
        screen.fill(BLACK)
        draw_snake(snake_body)
        draw_food(food_position)
        pygame.display.update()

        # Set the game frame rate
        clock.tick(30)

    game_over()


run_game()
