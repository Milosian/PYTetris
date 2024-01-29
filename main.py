import pygame as pg
import sys
import random

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

# Block's postion class
class Position:
    def __init__(self, row, column):
        self.row = row
        self.column = column
        
# Block class with all parameters        
class Block:
    def __init__(self, id):
        self.id = id
        self.cells = {}
        self.cellSize = 35
        self.row_offset = 0
        self.column_offset = 0
        self.rotation_offset = 0
        self.rotationState = 0
        self.colors = Colors.getCellColors()
    
    def move(self, rows, columns):
        self.row_offset += rows
        self.column_offset += columns
    
    def get_cell_position(self):
        tiles = self.cells[self.rotationState]
        moved_tiles = []
        for position in tiles:
            position = Position(position.row + self.row_offset, position.column + self.column_offset)   
            moved_tiles.append(position)
        return moved_tiles
    
    def rotate(self):
        self.rotationState += 1
        if self.rotationState == len(self.cells):
            self.rotaionState = 0
    
    def undo_rotation(self):
        self.rotationState -= 1
        if self.rotationState == 0:
            self.rotaionState = len(self.cells) -1
            
    def draw(self, window):
        tiles = self.get_cell_position()
        for tile in tiles:
            x = board_x + tile.column * self.cellSize + 1
            y = board_y + tile.row * self.cellSize + 1
            tileRect = pg.Rect(x, y, self.cellSize - 1, self.cellSize - 1)
            pg.draw.rect(window, self.colors[self.id], tileRect)

# Types of blocks      
class LBlock(Block):
    def __init__(self):
        super().__init__(id = 1)
        self.cells = {
            0: [Position(0, 2), Position(1, 0), Position(1, 1), Position(1, 2)],
            1: [Position(0, 1), Position(1, 1), Position(2, 1), Position(2, 2)],
            2: [Position(1, 0), Position(1, 1), Position(1, 2), Position(2, 0)],
            3: [Position(0, 0), Position(0, 1), Position(1, 1), Position(2, 1)]
        }
        self.move(0, 3)
        
class JBlock(Block):
    def __init__(self):
        super().__init__(id = 2)
        self.cells = {
            0: [Position(0, 0), Position(1, 0), Position(1, 1), Position(1, 2)],
            1: [Position(0, 1), Position(0, 2), Position(1, 1), Position(2, 1)],
            2: [Position(1, 0), Position(1, 1), Position(1, 2), Position(2, 2)],
            3: [Position(0, 1), Position(1, 1), Position(2, 0), Position(2, 1)]
        }
        self.move(0, 3)
        
class IBlock(Block):
    def __init__(self):
        super().__init__(id = 3)
        self.cells = {
            0: [Position(1, 0), Position(1, 1), Position(1, 2), Position(1, 3)],
            1: [Position(0, 2), Position(1, 2), Position(2, 2), Position(3, 2)],
            2: [Position(2, 0), Position(2, 1), Position(2, 2), Position(2, 3)],
            3: [Position(0, 1), Position(1, 1), Position(2, 1), Position(3, 1)]
        }
        self.move(-1, 3)
        
class OBlock(Block):
    def __init__(self):
        super().__init__(id = 4)
        self.cells = {
            0: [Position(0, 0), Position(0, 1), Position(1, 0), Position(1, 1)],
            1: [Position(0, 0), Position(0, 1), Position(1, 0), Position(1, 1)],
            2: [Position(0, 0), Position(0, 1), Position(1, 0), Position(1, 1)],
            3: [Position(0, 0), Position(0, 1), Position(1, 0), Position(1, 1)],
        }
        self.move(0, 4)
        
class SBlock(Block):
    def __init__(self):
        super().__init__(id = 5)
        self.cells = {
            0: [Position(0, 1), Position(0, 2), Position(1, 0), Position(1, 1)],
            1: [Position(0, 1), Position(1, 1), Position(1, 2), Position(2, 2)],
            2: [Position(1, 1), Position(1, 2), Position(2, 0), Position(2, 1)],
            3: [Position(0, 0), Position(1, 0), Position(1, 1), Position(2, 1)]
        }
        self.move(0, 3)
        
class TBlock(Block):
    def __init__(self):
        super().__init__(id = 6)
        self.cells = {
            0: [Position(0, 1), Position(1, 0), Position(1, 1), Position(1, 2)],
            1: [Position(0, 1), Position(1, 1), Position(1, 2), Position(2, 1)],
            2: [Position(1, 0), Position(1, 1), Position(1, 2), Position(2, 1)],
            3: [Position(0, 1), Position(1, 0), Position(1, 1), Position(2, 1)]
        }
        self.move(0, 3)
        
class ZBlock(Block):
    def __init__(self):
        super().__init__(id = 7)
        self.cells = {
            0: [Position(0, 0), Position(0, 1), Position(1, 1), Position(1, 2)],
            1: [Position(0, 2), Position(1, 1), Position(1, 2), Position(2, 1)],
            2: [Position(1, 0), Position(1, 1), Position(2, 1), Position(2, 2)],
            3: [Position(0, 1), Position(1, 0), Position(1, 1), Position(2, 0)]
        }
        self.move(0, 3)

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
    # Check if block is out of grid
    def positionCheck(self, row, columns):
        if row >= 0 and row < self.rows and columns >= 0 and columns < self.columns:
            return True
        return False
    
    def emptyCheck(self, row, columns):
        if self.grid[row][columns] == 0: 
            return True
        return False
   
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

# Gameplay functions
class Gameplay:
    def __init__(self):
        self.grid = TetrisBoard()
        self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        self.current_block = self.random_blocks()
        self.next_block = self.random_blocks()
    
    # Get random blocks
    def random_blocks(self):
        if len(self.blocks) == 0:
            self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        block =  random.choice(self.blocks)
        self.blocks.remove(block)
        return block
    
    # Moving blocks
    def moveLeft(self):
        self.current_block.move(0, -1)
        if self.block_check() ==  False or self.block_fits() == False:
            self.current_block.move(0, 1)
             
    def moveRight(self):
        self.current_block.move(0, 1)
        if self.block_check() ==  False or self.block_fits() == False:
            self.current_block.move(0, -1)
            
    def moveDown(self):
        self.current_block.move(1, 0)
        if self.block_check() ==  False or self.block_fits() == False:
            self.current_block.move(-1, 0)
            self.lockBlock()
    
    def rotate(self):
        self.current_block.rotate()
        if self.block_check() == False or self.block_fits() == False:
            self.current_block.undo_rotation()
    
    # Lock block if is maximum down
    def lockBlock(self):
        tiles = self.current_block.get_cell_position()
        for position in tiles:
            self.grid.grid[position.row][position.column] = self.current_block.id
        self.current_block = self.next_block
        self.next_block = self.random_blocks()
    
    def block_fits(self):
        tiles = self.current_block.get_cell_position()
        for tile in tiles:
            if self.grid.emptyCheck(tile.row, tile.column) == False:
                return False
        return True
    def block_check(self):
        tiles = self.current_block.get_cell_position()
        for tile in tiles:
            if self.grid.positionCheck(tile.row, tile.column) == False:
                return False
        return True
        
    def draw(self, window):
        self.grid.draw(window)
        self.current_block.draw(window)

clock = pg.time.Clock()        

game = Gameplay()

GAME_UPDATE = pg.USEREVENT
pg.time.set_timer(GAME_UPDATE, 200)
# Main game loop
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        # Keys functions 
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                game.moveLeft()
            if event.key == pg.K_RIGHT:
                game.moveRight()
            if event.key == pg.K_DOWN:
                game.moveDown()
            if event.key == pg.K_UP:
                game.rotate()
        if event.type == GAME_UPDATE:
            game.moveDown()
            
    window.fill((0, 40, 20))  # Clear the window

    game.draw(window)
    # tetris_board.draw(window)  # Draw the Tetris board
    # block.draw(window)
    pg.display.update()
    clock.tick(60)
