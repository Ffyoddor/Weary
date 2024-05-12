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

screen.fill(BLUE)

pygame.draw.rect(screen, (255,255,255),
                                (20,20,100,75), 5)

pygame.draw.lines(screen, (0,0,0),  [[10,100], [140,170],[280,110]])

pygame.draw.aalines(screen, (0,0,0),True,[[10,100], [140,170],[280,110]])

pygame.display.update()

while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()


