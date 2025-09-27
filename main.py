import pygame

pygame.init()
pygame.font.init()

from src.window import Window

window = Window((640, 480))
window.fill((255, 255, 255))
window.update()

clock = pygame.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    window.handle_event(None)

    clock.tick(12)