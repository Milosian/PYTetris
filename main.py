import pygame as pg
import sys

# Initialize Pygame
pg.init()

# Setting up window dimensions and parameters
pg.display.set_caption("Tetris")
window_width, window_height = 800, 850
board_width, board_height = 750, 750
board_x = (window_width - board_width)
board_y = (window_height - board_height)

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
        # Draw the grid lines and block textures on the window
        for row in range(self.rows):
            for column in range(self.columns):
                x = board_x + column * self.cell_size
                y = board_y + row * self.cell_size
                pg.draw.rect(window, (255, 255, 255), (x, y, self.cell_size, self.cell_size), 1)
                if self.grid[row][column] != 0:
                    block_texture = block_textures[self.grid[row][column]]
                    window.blit(block_texture, (x, y))

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
