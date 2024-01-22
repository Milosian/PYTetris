import pygame as pg;
import sys

pg.init();

#Setting window, board, shapes parametres
pg.display.set_caption("Tetris");
width, height = 800, 850
boardWidth, boardHeight = 400, 800
colums, rows = 10, 20
X = (width - boardWidth)
Y = (height - boardHeight)

window = pg.display.set_mode((width, height))

clock = pg.time.Clock()
#Dictionary of block's textures
textures = {
    'I' : pg.image.load("assets/I.png"),
    'J' : pg.image.load("assets/J.png"),
    'L' : pg.image.load("assets/L.png"),
    'O' : pg.image.load("assets/O.png"),
    'S' : pg.image.load("assets/S.png"),
    'T' : pg.image.load("assets/T.png"),
    'Z' : pg.image.load("assets/Z.png"),
}

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    pg.display.update()
    clock.tick(60)