import pygame
import random

# Initialize Pygame
pygame.init()

# Set the dimensions of the window
window_width = 640
window_height = 480
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Randomly Generated Maze Game")

# Set colors
background_color = (255, 255, 255)
wall_color = (0, 0, 0)
player_color = (255, 0, 0)
exit_color = (0, 255, 0)

# Set the dimensions of the maze
maze_width = 20
maze_height = 15

# Set the size of each cell in the maze
cell_size = 20

# Set the starting position of the player
player_x = 1
player_y = 1

# Generate the maze
maze = [[0] * maze_width for _ in range(maze_height)]

# Set the outer walls of the maze
for i in range(maze_width):
    maze[0][i] = 1
    maze[maze_height - 1][i] = 1
for i in range(maze_height):
    maze[i][0] = 1
    maze[i][maze_width - 1] = 1

# Recursive backtracking algorithm to generate the maze
def generate_maze(x, y):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    random.shuffle(directions)
    for dx, dy in directions:
        next_x = x + dx * 2
        next_y = y + dy * 2
        if 0 < next_x < maze_width - 1 and 0 < next_y < maze_height - 1 and maze[next_y][next_x] == 0:
            maze[y + dy][x + dx] = 1
            maze[next_y][next_x] = 1
            generate_maze(next_x, next_y)

generate_maze(player_x, player_y)

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the window
    window.fill(background_color)

    # Draw the maze
    for y in range(maze_height):
        for x in range(maze_width):
            if maze[y][x] == 1:
                pygame.draw.rect(window, wall_color, (x * cell_size, y * cell_size, cell_size, cell_size))

    # Draw the player
    pygame.draw.rect(window, player_color, (player_x * cell_size, player_y * cell_size, cell_size, cell_size))

    # Draw the exit
    pygame.draw.rect(window, exit_color, ((maze_width - 2) * cell_size, (maze_height - 2) * cell_size, cell_size, cell_size))

    # Update the display
    pygame.display.update()

    # Handle player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and maze[player_y - 1][player_x] == 0:
        player_y -= 1
    if keys[pygame.K_DOWN] and maze[player_y + 1][player_x] == 0:
        player_y += 1
    if keys[pygame.K_LEFT] and maze[player_y][player_x - 1] == 0:
        player_x -= 1
    if keys[pygame.K_RIGHT] and maze[player_y][player_x + 1] == 0:
        player_x += 1

    # Check if the player reached the exit
    if player_x == maze_width - 2 and player_y == maze_height - 2:
        running = False

# Quit the game
pygame.quit()
