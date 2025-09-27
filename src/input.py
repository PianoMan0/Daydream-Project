import pygame
import json
from .palette import Palette

font = pygame.font.Font("clangen.ttf", 20)


class Input:
    def __init__(self, data) -> None:
        """ options: ["text", "file_to_change_to"]"""
        self.options = data["options"]
        self.surface = pygame.Surface((800, 0), pygame.SRCALPHA)
        self.surface.fill((255, 0, 0))
        self.textsurf = pygame.Surface((800, 0), pygame.SRCALPHA)
        self.height = 0
        self.waiting = True
        self.drawing = True
        self.selected = 0
        for line in self.options:
            chars = f"> {line[0]}"
            text = font.render(chars, True, Palette.text)
            self.extend_surf(text.height + 4)
            self.textsurf.blit(text, (0, self.height))
            self.height += text.height + 4
    
    def extend_surf(self, height: int):
        _textsurface = pygame.Surface((self.textsurf.width, self.textsurf.height + height), pygame.SRCALPHA)
        _surface = pygame.Surface((self.surface.width, self.surface.height + height), pygame.SRCALPHA)
        _textsurface.blit(self.textsurf, (0, 0))
        _surface.blit(self.surface, (0, 0))
        self.textsurf = _textsurface
        self.surface = _surface

    def draw(self):
        pygame.draw.rect(self.surface, (255, 255, 255), (0, self.selected*24 + 4, 10, 20))
        self.surface.blit(self.textsurf, (0, 0))
        return self.surface

    def handle_event(self, event) -> None:
        if event is None: return
        if event.type == pygame.KEYDOWN:
            self.surface.fill(Palette.background)
            if event.key == pygame.K_UP:
                self.selected = max(self.selected - 1, 0)
            if event.key == pygame.K_DOWN:
                self.selected = min(self.selected + 1, len(self.options) - 1)
            if event.key == pygame.K_RETURN:
                self.waiting = False
                self.file = self.options[self.selected][1]
