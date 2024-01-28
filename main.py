import pygame as pg
import sys

# Initialize Pygame
pg.init()

# Setting up window dimensions and parameters
pg.display.set_caption("Tetris")
window_width, window_height = 850, 800
board_width, board_height = 750, 750
holder_width, holder_height = 150, 150
scoreboard_width, scoreboard_height = 150, 250
next_width, next_height = 150, 300
board_x, board_y = 250, 50
holder_x, holder_y = 50, 100
scoreboard_x, scoreboard_y = 50, 400
next_x, next_y = 650, 100

# Create the game window
window = pg.display.set_mode((window_width, window_height))

# Set up the game clock
clock = pg.time.Clock()

# Dictionary of block textures
block_textures = {
    'I': pg.image.load("assets/I.png"),
    'J': pg.image.load("assets/J.png"),
    'L': pg.image.load("assets/L.png"),
    'O': pg.image.load("assets/O.png"),
    'S': pg.image.load("assets/S.png"),
    'T': pg.image.load("assets/T.png"),
    'Z': pg.image.load("assets/Z.png"),
}

class TetrisBoard:
    def __init__(self):
        # Set up the game board parameters
        self.rows = 20
        self.columns = 10
        self.cell_size = 35
        self.grid = [[0 for _ in range(self.columns)] for _ in range(self.rows)]

    def draw_grid(self):
        # Draw the grid lines on the window
        for row in range(self.rows):
            for column in range(self.columns):
                x = board_x + column * self.cell_size
                y = board_y + row * self.cell_size
                pg.draw.rect(window, (255, 255, 255), (x, y, self.cell_size, self.cell_size), 1)

        pg.draw.rect(window, (255, 255, 255), (holder_x, holder_y, holder_width, holder_height))
        pg.draw.rect(window, (255, 255, 255), (holder_x, holder_y, holder_width, holder_height), 1)
        inner_width = holder_width - 2
        inner_height = holder_height - 2
        pg.draw.rect(window, (0, 0, 0), (holder_x + 1, holder_y + 1, inner_width, inner_height))

        pg.draw.rect(window, (255, 255, 255), (scoreboard_x, scoreboard_y, scoreboard_width, scoreboard_height))
        pg.draw.rect(window, (255, 255, 255), (scoreboard_x, scoreboard_y, scoreboard_width, scoreboard_height), 1)
        inner_width = scoreboard_width - 2
        inner_height = scoreboard_height - 2
        pg.draw.rect(window, (0, 0, 0), (scoreboard_x + 1, scoreboard_y + 1, inner_width, inner_height))


        pg.draw.rect(window, (255, 255, 255), (next_x, next_y, next_width, next_height))
        pg.draw.rect(window, (255, 255, 255), (next_x, next_y, next_width, next_height), 1)
        inner_width = next_width - 2
        inner_height = next_height - 2
        pg.draw.rect(window, (0, 0, 0), (next_x + 1, next_y + 1, inner_width, inner_height))

# Create an instance of the TetrisBoard class
tetris_board = TetrisBoard()

# Main game loop
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    window.fill((0, 0, 0))  # Clear the window

    tetris_board.draw_grid()  # Draw the Tetris board

    pg.display.update()
    clock.tick(60)
