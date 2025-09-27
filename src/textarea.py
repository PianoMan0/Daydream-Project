import pygame
from .text import Line
from .input import Input
from .utils import load_lines_from_file
from .inventory import Inventory, AddItem, RemoveItem
from .redirect import Redirect

class TextArea:
    def __init__(self, window, width: int):
        self.window = window
        self.surface = pygame.Surface((width, 0), flags=pygame.SRCALPHA)
        self.font_size = 20
        self.line_height = 20
        self.lines = load_lines_from_file("lines/A.json")
        self.total_height = 0
        self.current_line = None
        self.inventory = Inventory()

    def draw_most_recent(self) -> None:
        lines = list(filter(lambda x: x.drawing != False, self.lines))
        if len(lines) == 0: return
        line: Line = lines[0]
        if type(line) == Line:
            if self.current_line != line:
                self.extend_surf(line.surface.height)
                self.current_line = line
            if line.drawing != False:
                line.draw_next()
                self.surface.blit(line.surface, (0, self.total_height - line.surface.height))
            else:
                pass
        if type(line) == Input:
            if self.current_line != line:
                self.extend_surf(line.surface.height)
                self.current_line = line
            if line.waiting:
                self.surface.blit(line.draw(), (0, self.total_height - line.surface.height))
            else:
                self.lines = load_lines_from_file(line.file)
                line.drawing = False
        if type(line) == AddItem:
            self.inventory.add_item(line.item)
            if self.inventory.check_dead():
                self.lines = load_lines_from_file("lines/dead.json")
            line.drawing = False
        if type(line) == RemoveItem:
            self.inventory.remove_item(line.item)
            line.drawing = False
        if type(line) == Redirect:
            self.lines = load_lines_from_file(line.file)
            line.drawing = False

    def handle_event(self, event):
        if self.current_line: self.current_line.handle_event(event)

    def draw(self) -> None:
        self.window.blit(self.surface, (0, self.window.height - self.total_height))
        self.window.blit(self.inventory.draw(), (0, 0))

    def extend_surf(self, height: int):
        _surface = pygame.Surface((self.surface.width, self.surface.height + height), pygame.SRCALPHA)
        _surface.blit(self.surface, (0, 0))
        self.surface = _surface
        self.total_height += height