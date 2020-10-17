import pygame, player, world
from pygame.locals import *


"""
1 = murs (blanc)
2 = plafond (bleu)
3 = sol (vert)
4 = objet (rouge)
"""

def start():
    pygame.init()
    pygame.display.set_caption("3DEngine")

def drawScreen(screen, player, world):
    screen.fill((0, 0, 0))
    view = player.view(world)
    for i in range(120):
        for j in range(120):
            pygame.draw.rect(screen, view[i][j], (i*5, j*5, 5, 5))

def engine():
    p = player.Player()
    w = world.World((5, 100, 100))
    w.addCube((0, 7, 8), (4, 2, 1), 4)
    screen = pygame.display.set_mode((600, 600))
    pygame.mouse.set_visible(0)
    pygame.mouse.set_pos(300, 300)
    continuer = True
    while continuer:
        for event in pygame.event.get():
            if event.type == QUIT:
                continuer = False
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    p.move((0, 0, 1), w)
                elif event.key == K_DOWN:
                    p.move((0, 0, -1), w)
                elif event.key == K_LEFT:
                    p.move((0, 1, 0), w)
                elif event.key == K_RIGHT:
                    p.move((0, -1, 0), w)
        drawScreen(screen, p, w)
        pygame.display.update()
start()
engine()

# TODO : Faire rotation de la caméra
