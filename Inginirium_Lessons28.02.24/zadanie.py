import pygame
import random

W, H = 500, 500

pygame.init()
win = pygame.display.set_mode((W, H))
object_to_drow ='kvadrat'
while 1:

    keys = pygame.key.get_pressed()
    if keys [pygame.K_w]:
        object_to_drow = 'krug'
    elif keys[pygame.K_q]:
        object_to_drow = 'kvadrat'

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    pos = pygame.mouse.get_pos()
    x = pos[0]
    y = pos[1]
    if object_to_drow == 'kvadrat':
        ...#pygame.draw.rect()
    if object_to_drow == 'krug':
        pygame.draw.circle(win, random.choices(range(256), k = 3), (x, y), 30)

#pressed = pygame.mouse.get_pressed()
    #if pressed[0]:
    #    pos = pygame.mouse.get_pos()
    #    pygame.draw.circle(win, WHITE, pos, 5)
    pygame.display.update()

    pygame.time.delay(20)
