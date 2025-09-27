import pygame

font = pygame.font.SysFont("clangen.ttf", 20)

class Window:
    def __init__(self, size: tuple[int, int]) -> None:
        self.window = pygame.display.set_mode((640, 480), flags=pygame.SRCALPHA)
        self.lines = []
    
    def fill(self, color) -> None:
        self.window.fill(color)
    
    def draw_lines(self) -> None:
        for line in self.lines:
            text = font.render(line)
            ...