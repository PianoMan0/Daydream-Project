import pygame
import asyncio
from src.palette import Palette

pygame.init()
pygame.font.init()

from src.window import Window

clock = pygame.Clock()
window = Window((800, 600))

async def main():
    while True:
        window.fill(Palette.background)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            window.handle_event(event)
        window.draw()
        pygame.display.update()

        clock.tick(20)
        await asyncio.sleep(0)

asyncio.run(main())