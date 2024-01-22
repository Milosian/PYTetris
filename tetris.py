import pygame as pg;
import sys

pg.init();

width, height = 800, 850

board = pg.display.set_mode((width, height))
pg.display.set_caption("Tetris");
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
colums, rows = 10, 20
