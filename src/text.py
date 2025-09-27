import pygame
from src.palette import Palette

font = pygame.font.Font("clangen.ttf", 20)

class Line:
    def __init__(self, data):
        self.text = data["text"]
        self.auto = data.get("auto")
        self.delay = data.get("delay")
        textsurface = font.render(self.text, True, Palette.text)
        self.surface = pygame.Surface(textsurface.size)
        self.surface.fill(Palette.background)
        self.character_index = 0
        self.current_x = 0
        self.drawing = True
        self.current_delay = 0

    def draw_next(self):
        if self.drawing is True:
            char = font.render(self.text[self.character_index], True, Palette.text)
            self.surface.blit(char, (self.current_x, 0))
            self.character_index += 1
            self.current_x += char.width
        if self.character_index >= len(self.text): self.drawing = None
        if self.drawing is None:
            delay = self.handle_delay()
            if delay: self.drawing = False
    
    def handle_delay(self):
        if not self.auto: return True 
        if self.current_delay < self.delay:
            self.current_delay += 1
            return False
        return True