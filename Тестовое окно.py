import pygame
import sys

FPS=60

W = 700
H = 300

WHITE = (255, 255, 255)
BLUE = (0, 70, 225)

screen = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()

x = W //2
y = H//2
r = 50

while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()
        elif i