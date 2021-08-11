import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):

    def __init__(self, shooting):

        super().__init__()
        self.screen = shooting.screen
        self.settings = shooting.settings
        self.color = self.settings.bullet_color

        # Создание снаряда ри расположение его у центра правого края корабля
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midleft = shooting.ship.rect.midright

        self.x = float(self.rect.x)

    def update(self):
        """обновление позиции снаряда"""
        self.x += self.settings.bullet_speed

        self.rect.x = self.x

    def draw_bullet(self):
        """Отрисовка снаряда"""
        pygame.draw.rect(self.screen, self.color, self.rect)