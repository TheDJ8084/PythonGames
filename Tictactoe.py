import pygame
import os
import subprocess

# Initialize Pygame
pygame.init()

# Set up the game window
window_width = 300
window_height = 300
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Tic Tac Toe")

# Set up the colors
background_color = (255, 255, 255)
line_color = (0, 0, 0)
x_color = (255, 0, 0)
o_color = (0, 0, 255)
win_color = (0, 255, 0)
text_color = (0, 0, 0)

# Set up the game variables
board = [['', '', ''], ['', '', ''], ['', '', '']]
current_player = 'X'
game_over = False
winner = None
message = None

# Set up the font
font = pygame.font.Font(None, 48)

def draw_board():
    window.fill(background_color)
    pygame.draw.line(window, line_color, (window_width / 3, 0), (window_width / 3, window_height), 3)
    pygame.draw.line(window, line_color, (2 * window_width / 3, 0), (2 * window_width / 3, window_height), 3)
    pygame.draw.line(window, line_color, (0, window_height / 3), (window_width, window_height / 3), 3)
    pygame.draw.line(window, line_color, (0, 2 * window_height / 3), (window_width, 2 * window_height / 3), 3)
    
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'X':
                pygame.draw.line(window, x_color, (j * window_width / 3 + 20, i * window_height / 3 + 20),
                                 ((j + 1) * window_width / 3 - 20, (i + 1) * window_height / 3 - 20), 5)
                pygame.draw.line(window, x_color, ((j + 1) * window_width / 3 - 20, i * window_height / 3 + 20),
                                 (j * window_width / 3 + 20, (i + 1) * window_height / 3 - 20), 5)
            elif board[i][j] == 'O':
                pygame.draw.circle(window, o_color, (int(j * window_width / 3 + window_width / 6),
                                                     int(i * window_height / 3 + window_height / 6)), int(window_width / 6 - 20), 3)
                
    if message:
        text_surface = font.render(message, True, text_color)
        text_rect = text_surface.get_rect(center=(window_width / 2, window_height / 2))
        window.blit(text_surface, text_rect)
        
def check_win():
    global winner
    
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != '':
            winner = board[i][0]
            return True
        
        if board[0][i] == board[1][i] == board[2][i] != '':
            winner = board[0][i]
            return True
        
    if board[0][0] == board[1][1] == board[2][2] != '':
        winner = board[0][0]
        return True
    
    if board[0][2] == board[1][1] == board[2][0] != '':
        winner = board[0][2]
        return True
    
    if all(board[i][j] != '' for i in range(3) for j in range(3)):
        winner = 'draw'
        return True
    
    return False

def switch_player():
    global current_player
    if current_player == 'X':
        current_player = 'O'
    else:
        current_player = 'X'
        
def restart_game():
    global board, current_player, game_over, winner, message
    board = [['', '', ''], ['', '', ''], ['', '', '']]
    current_player = 'X'
    game_over = False
    winner = None
    message = None

def open_another_file():
    # Open another Python file after the game ends
    subprocess.Popen(['python', 'Multiplayergames.py'])
    pygame.quit()
    os._exit(0)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            if pygame.mouse.get_pressed()[0]:
                x, y = pygame.mouse.get_pos()
                row = int(y // (window_height / 3))
                col = int(x // (window_width / 3))
                if board[row][col] == '':
                    board[row][col] = current_player
                    if check_win():
                        if winner == 'draw':
                            message = "It's a draw!"
                        else:
                            message = f"{winner} wins!"
                        game_over = True
                        open_another_file()
                    else:
                        switch_player()
                        
    draw_board()
    pygame.display.flip()
