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

class Colors:
    white = (0, 0, 0)
    blue = (56, 155, 217)
    indigo = (56, 75, 217)
    orange = (217, 99, 56)
    yellow = (217, 211, 56)
    green = (56, 217, 64)
    purple = (153, 56, 217)
    red = (217, 56, 56)
    
    @classmethod
    def getCellColors(cls):
        return [cls.white, cls.blue, cls.indigo, cls.orange, cls.yellow, cls.green, cls.purple, cls.red]

class Position:
    def __init__(self, row, column):
        self.row = row
        self.column = column
        
class Block:
    def __init__(self, id):
        self.id = id
        self.cells = {}
        self.cellSize = 35
        self.rotaionState = 0
        self.colors = Colors.getCellColors()
    
    def draw(self, screen):
        tiles = self.cells[self.rotaionState]
        for tile in tiles:
            x = board_x + tile.column * self.cellSize + 1
            y = board_y + tile.row * self.cellSize + 1
            tileRect = pg.Rect(x, y, self.cellSize - 1, self.cellSize - 1)
            pg.draw.rect(window, self.colors[self.id], tileRect)
        
class LBlock(Block):
    def __init__(self):
        super().__init__(id = 1)
        self.cells = {
            0: [Position(0, 2), Position(1, 0), Position(1, 1), Position(1, 2)],
            1: [Position(0, 1), Position(1, 1), Position(2, 1), Position(2, 2)],
            2: [Position(1, 0), Position(1, 1), Position(1, 2), Position(2, 0)],
            3: [Position(0, 0), Position(0, 1), Position(1, 1), Position(2, 1)]
        }
class TetrisBoard:
    def __init__(self):
        # Set up the game board parameters
        self.rows = 20
        self.columns = 10
        self.cell_size = 35
        self.grid = [[0 for j in range(self.columns)] for i in range(self.rows)]
        self.colors = Colors.getCellColors()
    
    # print block int grid 
    def draw_block(self):
        for row in range(self.rows):
            for column in range(self.columns):
                print(self.grid[row][column], end = " ")
            print()  
        
    def draw(self, window):
        # Draw the grid lines on the window
        for row in range(self.rows):
            for column in range(self.columns):
                cellValue = self.grid[row][column]
                x = board_x + column*self.cell_size +1
                y = board_y + row*self.cell_size +1
                cellRect = pg.Rect(x, y, self.cell_size -1, self.cell_size -1)
                pg.draw.rect(window, self.colors[cellValue], cellRect)
                
        # Draw the block holder 
        pg.draw.rect(window, (255, 255, 255), (holder_x, holder_y, holder_width, holder_height))
        pg.draw.rect(window, (255, 255, 255), (holder_x, holder_y, holder_width, holder_height), 1)
        inner_width = holder_width - 2
        inner_height = holder_height - 2
        pg.draw.rect(window, (0, 15, 0), (holder_x + 1, holder_y + 1, inner_width, inner_height))

        # Draw the scoreboard
        pg.draw.rect(window, (255, 255, 255), (scoreboard_x, scoreboard_y, scoreboard_width, scoreboard_height))
        pg.draw.rect(window, (255, 255, 255), (scoreboard_x, scoreboard_y, scoreboard_width, scoreboard_height), 1)
        inner_width = scoreboard_width - 2
        inner_height = scoreboard_height - 2
        pg.draw.rect(window, (0, 15, 0), (scoreboard_x + 1, scoreboard_y + 1, inner_width, inner_height))

        # Draw the window for next block
        pg.draw.rect(window, (255, 255, 255), (next_x, next_y, next_width, next_height))
        pg.draw.rect(window, (255, 255, 255), (next_x, next_y, next_width, next_height), 1)
        inner_width = next_width - 2
        inner_height = next_height - 2
        pg.draw.rect(window, (0, 15, 0), (next_x + 1, next_y + 1, inner_width, inner_height))

# Create an instance of the TetrisBoard class
tetris_board = TetrisBoard()

# Draw example blocks in random area
block = LBlock()

tetris_board.draw_block()

# Main game loop
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    window.fill((0, 40, 20))  # Clear the window

    tetris_board.draw(window)  # Draw the Tetris board
    block.draw(window)
    pg.display.update()
    clock.tick(60)
