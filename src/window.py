import pygame
from .text import Line

class Window:
    def __init__(self, size: tuple[int, int]) -> None:
        self.window = pygame.display.set_mode(size, flags=pygame.SRCALPHA)
        self.font_size = 20
        self.line_height = 20
        self.lines = [
            Line("this is a test")
        ]
    
    def fill(self, color) -> None:
        self.window.fill(color)
    
    def handle_event(self, e):
        self.draw_most_recent_line()
    
    def draw_most_recent_line(self) -> None:
        line = self.lines[-1]
        if line.drawing:
            line.draw_next()
            self.fill((255, 255, 255))
            self.window.blit(line.surface, (0, 0))
            self.update()
        else:
            pass

    def update(self, area: None = None) -> None:
        if area is None:
            pygame.display.update()
        else: 
            pygame.display.update(area)