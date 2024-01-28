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
# block_textures = {
#     'I': pg.image.load("assets/I.png"),
#     'J': pg.image.load("assets/J.png"),
#     'L': pg.image.load("assets/L.png"),
#     'O': pg.image.load("assets/O.png"),
#     'S': pg.image.load("assets/S.png"),
#     'T': pg.image.load("assets/T.png"),
#     'Z': pg.image.load("assets/Z.png"),
# }

class Block:
    def __init__(self, id):
        self.id = id
        self.cells = {}
        self.cellSize = 30
        self.rotaionState = 0
class Colors:
    blue = (56, 155, 217)
    indigo = (56, 75, 217)
    orange = (217, 99, 56)
    yellow = (217, 211, 56)
    green = (56, 217, 64)
    purple = (153, 56, 217)
    red = (217, 56, 56)
    
    @classmethod
    def getCellColors(cls):
        return [cls.blue, cls.green, cls.yellow, cls.indigo, cls.orange, cls.red, cls.purple]

        
class TetrisBoard:
    def __init__(self):
        # Set up the game board parameters
        self.rows = 20
        self.columns = 10
        self.cell_size = 35
        self.grid = [[0 for j in range(self.columns)] for i in range(self.rows)]
        self.colors = Colors.getCellColors() 

    def draw_block(self):
        for row in range(self.rows):
            for column in range(self.columns):
                print(self.grid[row][column], end = " ")
            print()  
            
    def draw_grid(self, window):
        # Draw the grid lines on the window
        for row in range(self.rows):
            for column in range(self.columns):
                x = board_x + column * self.cell_size
                y = board_y + row * self.cell_size
                cellRect = pg.Rect(x, y, self.cell_size, self.cell_size)
                pg.draw.rect(window, (255, 255, 255), cellRect, 1)
                
        # Draw the block holder 
        pg.draw.rect(window, (255, 255, 255), (holder_x, holder_y, holder_width, holder_height))
        pg.draw.rect(window, (255, 255, 255), (holder_x, holder_y, holder_width, holder_height), 1)
        inner_width = holder_width - 2
        inner_height = holder_height - 2
        pg.draw.rect(window, (0, 0, 0), (holder_x + 1, holder_y + 1, inner_width, inner_height))

        # Draw the scoreboard
        pg.draw.rect(window, (255, 255, 255), (scoreboard_x, scoreboard_y, scoreboard_width, scoreboard_height))
        pg.draw.rect(window, (255, 255, 255), (scoreboard_x, scoreboard_y, scoreboard_width, scoreboard_height), 1)
        inner_width = scoreboard_width - 2
        inner_height = scoreboard_height - 2
        pg.draw.rect(window, (0, 0, 0), (scoreboard_x + 1, scoreboard_y + 1, inner_width, inner_height))

        # Draw the window for next block
        pg.draw.rect(window, (255, 255, 255), (next_x, next_y, next_width, next_height))
        pg.draw.rect(window, (255, 255, 255), (next_x, next_y, next_width, next_height), 1)
        inner_width = next_width - 2
        inner_height = next_height - 2
        pg.draw.rect(window, (0, 0, 0), (next_x + 1, next_y + 1, inner_width, inner_height))

# Create an instance of the TetrisBoard class
tetris_board = TetrisBoard()

tetris_board.grid[0][0] = 1
tetris_board.grid[3][5] = 4
tetris_board.grid[17][8] = 7

tetris_board.draw_block()
# Main game loop
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    window.fill((0, 0, 0))  # Clear the window

    tetris_board.draw_grid(window)  # Draw the Tetris board

    pg.display.update()
    clock.tick(60)
