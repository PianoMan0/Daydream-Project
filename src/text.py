import pygame

font = pygame.font.Font("clangen.ttf", 20)

class Line:
    def __init__(self, text):
        self.text = text
        textsurface = font.render(text, True, (0, 0, 0))
        self.surface = pygame.Surface(textsurface.size)
        self.surface.fill((255, 255, 255))
        self.character_index = 0
        self.current_x = 0
        self.drawing = True

    def draw_next(self):
        if self.character_index >= len(self.text) - 1: self.drawing = False
        char = font.render(self.text[self.character_index], True, (0, 0, 0))
        self.surface.blit(char, (self.current_x, 0))
        self.character_index += 1
        self.current_x += char.width