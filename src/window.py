import pygame
from .text import Line
from .textarea import TextArea
from .utils import load_lines_from_file

class Window:
    def __init__(self, size: tuple[int, int]) -> None:
        self.window = pygame.display.set_mode(size, flags=pygame.SRCALPHA)
        self.textarea = TextArea(self.window, size[0])
    
    def fill(self, color) -> None:
        self.window.fill(color)
    
    def handle_event(self, e):
        self.textarea.draw_most_recent_line()

    def update(self, area: None = None) -> None:
        if area is None:
            pygame.display.update()
        else: 
            pygame.display.update(area)