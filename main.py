import pygame

pygame.init()
pygame.font.init()

from src.window import Window

window = Window((640, 480))

clock = pygame.Clock()

while True:
    window.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    window.handle_event(None)
    window.update()


    clock.tick(12)