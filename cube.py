import pygame
from pygame.sprite import Sprite


class Cube(Sprite):

    def __init__(self, shooting):
        super().__init__()
        self.screen = shooting.screen
        self.settings = shooting.settings
        self.color = shooting.settings.cub_color
        self.rect = pygame.Rect(0, 0, self.settings.cub_width, self.settings.cub_height)
        self.screen_rect = shooting.screen.get_rect()
        self.rect.midright = self.screen_rect.midright
        self.y = float(self.rect.y)

    def draw_cube(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

    def check_edges(self):
        if self.rect.top <= self.screen_rect.top or self.rect.bottom >= self.screen_rect.bottom:
            return True

    def cub_update(self):
        self.y += self.settings.cub_speed * self.settings.direction
        self.rect.y = self.y



