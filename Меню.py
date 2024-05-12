import pygame as pg
import sys
import random as rd

pg.init()


SHRIFT = pg.font.SysFont(None, 36)
WIDTH = 1300
HEIGHT = 768
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (125, 125, 125)
LIGHT_BLUE = (64, 128, 255)
GREEN = (0, 200, 64)
YELLOW = (225, 225, 0)
PINK = (230, 50, 230)

sc = pg.display.set_mode((WIDTH, HEIGHT), pg.FULLSCREEN, 1)

NEWGAME = pg.Rect((625,400, 150, 50))
LOADGAME = pg.Rect((625,500, 150, 50))
SETTINGS = pg.Rect((625,600, 150, 50))
EXITGAME = pg.Rect((625,700, 150, 50))
NEWGAMETXT =0
LOADGAMETXT=0
SETTINGSTXT=0
EXITGAMETXT= SHRIFT.render("Выход ", True, (BLACK) )
PLACEEXITGAMETXT=EXITGAMETXT.get_rect(center=(500,500))

background = pg.image.load("6.jpg")                  # !!! установите свое .jpg

all_sprites = pg.sprite.Group()
background = pg.transform.scale(background, (1920, 1080))
pg.display.update()

sc.blit(EXITGAMETXT, (0,0))

pg.display.update()

while True:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            sys.exit()
        if i.type == pg.MOUSEBUTTONDOWN:
            if EXITGAME.collidepoint(i.pos): #Отслеживание нажатия мыши в точке выхода из игры
                sys.exit()

    pg.draw.rect(background,(WHITE), (625,400, 150, 50))
    pg.draw.rect(background, (WHITE), (625, 500, 150, 50), )
    pg.draw.rect(background, (WHITE), (625, 600, 150, 50), )
    pg.draw.rect(background, (WHITE), (625, 700, 150, 50), )
    sc.blit(background,(0,0))
    sc.blit(EXITGAMETXT, (655, 715))
    all_sprites.draw(sc)
    pg.display.update()

