import pygame
import sys
import random

# Initialize the game
pygame.init()

# Set the width and height of the screen
screen_width = 720
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the title of the window
pygame.display.set_caption("Snake Game")

# Color definitions
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Snake block size
block_size = 20

# Font for displaying score
font_style = pygame.font.SysFont(None, 50)

# Clock to control game speed
clock = pygame.time.Clock()

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [screen_width/6, screen_height/3])

def gameLoop():
    # Game over flag
    game_over = False

    # Game success flag
    game_close = False

    # Initial coordinates for the snake
    x1 = 300
    y1 = 300

    # Snake initial velocity
    x1_change = 0
    y1_change = 0

    # Initial coordinates for the food
    foodx = round(random.randrange(0, screen_width - block_size) / 20.0) * 20.0
    foody = round(random.randrange(0, screen_height - block_size) / 20.0) * 20.0

    # List to store the snake blocks
    snake_List = []
    snake_Length = 1

    # Main game loop
    while not game_over:
        while game_close == True:
            screen.fill(black)
            message("You Lost! Press Q-Quit or C-Play Again", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
                game_close = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -block_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = block_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -block_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = block_size
                    x1_change = 0

        if x1 >= screen_width or x1 < 0 or y1 >= screen_height or y1 < 0:
            game_close
