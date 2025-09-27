import pygame
import json
from .palette import Palette

font = pygame.font.Font("clangen.ttf", 20)

class Inventory:
    def __init__(self) -> None:
        self.surface = pygame.Surface((800, 24))
        self.items = []
    
    def check_dead(self) -> None:
        return len(self.items) > 5

    def add_item(self, item: str) -> None:
        self.items += item
    
    def remove_item(self, item: str) -> None:
        if item in self.items:
            self.items.remove(item)
    
    def draw(self) -> None:
        self.surface.fill(Palette.text)
        text = font.render(" ".join(self.items), True, Palette.background)
        self.surface.blit(text, (0, 2))
        return self.surface

class AddItem:
    def __init__(self, data):
        self.item = data["item"]

class RemoveItem:
    def __init__(self, data):
        self.item = data["item"]