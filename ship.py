import pygame

class Ship():

    def __init__(self, shooting):

        self.screen = shooting.screen
        self.settings = shooting.settings
        self.screen_rect = shooting.screen.get_rect()

        # Загрузка изображения корабля
        self.image = pygame.image.load('images/sprite_ship.bmp')
        # Поворот изображения
        self.rotated_image = pygame.transform.rotate(self.image, -90)

        self.rect = self.rotated_image.get_rect()

        # Расположение корабля в центре левого края
        self.rect.midleft = self.screen_rect.midleft

        self.y = float(self.rect.y)

        # Флаги движения
        self.moving_up = False
        self.moving_down = False

    def blitme(self):
        """Отрисовка корабля"""
        self.screen.blit(self.rotated_image, self.rect)

    def update_ship(self):
        """Обновление позиции корабля"""
        if self.moving_up and self.rect.top >= self.screen_rect.top:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom <= self.screen_rect.bottom:
            self.y += self.settings.ship_speed
        self.rect.y = self.y

    def center_ship(self):
        """Возврат корабля в центр при новой игре"""
        self.rect.midleft = self.screen_rect.midleft
        self.y = float(self.rect.y)

