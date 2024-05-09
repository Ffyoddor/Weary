#Шкелет программы
import pygame
from random import randint
pygame.init()

WIDHT, HEIGHT = 600,400
FPS=60

window = pygame.display.set_mode((WIDHT, HEIGHT))
clock = pygame.time.Clock()

play = True
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
    pygame.display.update()
    clock.tick(FPS)

pygame.quit