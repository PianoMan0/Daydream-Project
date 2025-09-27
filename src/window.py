import pygame


class Window:
    def __init__(self, size: tuple[int, int]) -> None:
        self.window = pygame.display.set_mode(size, flags=pygame.SRCALPHA)
        self.font_size = 20
        self.line_height = 20
        self.font = pygame.font.Font("clangen.ttf", self.font_size)
        self.lines = [
            "test 1",
            "test 2"
        ]
    
    def fill(self, color) -> None:
        self.window.fill(color)

    def update(self) -> None:
        pygame.display.update()
    
    def draw_lines(self) -> None:
        y = 0
        for line in self.lines:
            line = self.font.render(line, True, (0, 0, 0))
            self.window.blit(line, (0, y))
            y += self.line_height