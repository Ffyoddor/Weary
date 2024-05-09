#Шкелет программы
import pygame
from random import randint
pygame.init()

WIDHT, HEIGHT = 600,400
FPS=60

window = pygame.display.set_mode((WIDHT, HEIGHT))
clock = pygame.time.Clock()

cursorPX, cursorPY = WIDHT //2, HEIGHT // 2 #Peremennie dlya okr

def sight(x, y): #Функция отрисовки прицела
    pygame.draw.circle(window, (255, 255, 255), (x, y), 20, 1)
    pygame.draw.circle(window, (255, 255, 255), (x, y), 20, 1)
    pygame.draw.line(window, (255, 255, 255), (x - 24, y), (x - 16, y))
    pygame.draw.line(window, (255, 255, 255), (x + 24, y), (x + 16, y))
    pygame.draw.line(window, (255, 255, 255), (x, y - 24), (x, y - 16))
    pygame.draw.line(window, (255, 255, 255), (x, y + 24), (x, y + 16))

pygame.mouse.set_visible(False) #Pokazivaet vidimost mishi ot True and FAlse
play = True
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False


    cursorPX, cursorPY = pygame.mouse.get_pos()

    buttonLeft, buttonMiddle, buttonRight = pygame.mouse.get_pressed()
    print(buttonLeft, buttonMiddle, buttonRight)



    window.fill(pygame.Color('black'))

    sight(cursorPX, cursorPY)
    pygame.display.update()
    clock.tick(FPS)

pygame.quit