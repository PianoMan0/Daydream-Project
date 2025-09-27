import pygame
from .text import Line
from .utils import load_lines_from_file

class TextArea:
    def __init__(self, window, width: int):
        self.window = window
        self.surface = pygame.Surface((width, 0), flags=pygame.SRCALPHA)
        self.font_size = 20
        self.line_height = 20
        self.lines = load_lines_from_file("lines.json")
        self.total_height = 0
        self.current_line = None
    
    def fill(self, color) -> None:
        self.window.fill(color)

    def draw_most_recent_line(self) -> None:
        lines = list(filter(lambda x: x[1].drawing != False, enumerate(self.lines)))
        if len(lines) == 0: return
        line: Line = lines[0][1]
        index = lines[0][0]
        if self.current_line != line:
            self.extend_surf(line.surface.height)
            self.current_line = line
        if line.drawing != False:
            line.draw_next()
            self.fill((255, 255, 255))
            self.window.blit(line.surface, (0, index*self.line_height))
            self.update((0, index*self.line_height, *line.surface.size))
        else:
            pass
    
    def extend_surf(self, height: int):
        _surface = pygame.Surface((self.surface.width, self.surface.height + height))
        _surface.blit(self.surface, (0, 0))
        self.surface = _surface
        self.total_height += height

    def update(self, area: None = None) -> None:
        if area is None:
            pygame.display.update()
        else: 
            pygame.display.update(area)