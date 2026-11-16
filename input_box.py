import pygame

class InputBox:
    def __init__(self, x: int, y: int, w: int, h: int, color_active: tuple, color_inactive: tuple, prewritten_text: str = ""):
        self.color_active = pygame.Color(color_active)
        self.color_inactive = pygame.Color(color_inactive)
        self.color = self.color_active
        self.rect = pygame.Rect(x, y, w, h)

    def handle_input(self, input):
        if input.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoiint
    def draw(self):
        pygame.draw.rect(Surface, color, Rect, width=0)

    def color_change(self, color_active: tuple, color_inactive = tuple):
        self.color_active = color_active
        self.color_inactive = color_inactive