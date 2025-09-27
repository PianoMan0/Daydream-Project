import pygame
from src.palette import Palette

pygame.init()
pygame.font.init()

from src.window import Window

window = Window((640, 480))

clock = pygame.Clock()

while True:
    window.fill(Palette.background)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        window.handle_event(event)
    window.draw()
    window.update()


    clock.tick(0)