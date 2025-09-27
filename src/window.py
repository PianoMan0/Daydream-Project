import pygame
from .text import Line
from .utils import load_lines_from_txt

class Window:
    def __init__(self, size: tuple[int, int]) -> None:
        self.window = pygame.display.set_mode(size, flags=pygame.SRCALPHA)
        self.font_size = 20
        self.line_height = 20
        self.lines = load_lines_from_txt("lines.txt")
    
    def fill(self, color) -> None:
        self.window.fill(color)
    
    def handle_event(self, e):
        self.draw_most_recent_line()
    
    def draw_most_recent_line(self) -> None:
        lines = list(filter(lambda x: x[1].drawing, enumerate(self.lines)))
        if len(lines) == 0: return
        line = lines[0][1]
        index = lines[0][0]
        if line.drawing:
            line.draw_next()
            self.fill((255, 255, 255))
            self.window.blit(line.surface, (0, index*self.line_height))
            self.update((0, index*self.line_height, *line.surface.size))
        else:
            pass

    def update(self, area: None = None) -> None:
        if area is None:
            pygame.display.update()
        else: 
            pygame.display.update(area)