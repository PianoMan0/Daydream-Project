import pygame

pygame.init()
pygame.font.init()

from src.window import

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
