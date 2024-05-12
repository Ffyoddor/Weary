import pygame
import sys

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (125, 125, 125)
LIGHT_BLUE = (64, 128, 255)
GREEN = (0, 200, 64)
YELLOW = (225, 225, 0)
PINK = (230, 50, 230)
FPS = 60

W=600
H=600
x=0

pygame.init()
sc = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()
pygame.draw.rect(sc,(PINK),(0,50,50,50))
pygame.display.update()

while True:

    clock.tick(FPS)

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()





