import pygame

class Ship():

    def __init__(self, shooting):

        self.screen = shooting.screen
        self.settings = shooting.settings
        self.screen_rect = shooting.screen.get_rect()

        self.image = pygame.image.load('images/sprite_ship.bmp')
        self.rotated_image = pygame.transform.rotate(self.image, -90)

        self.rect = self.rotated_image.get_rect()

        self.rect.midleft = self.screen_rect.midleft

        self.y = float(self.rect.y)

        self.moving_up = False
        self.moving_down = False

    def blitme(self):
        self.screen.blit(self.rotated_image, self.rect)

    def update_ship(self):

        if self.moving_up and self.rect.top >= self.screen_rect.top:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom <= self.screen_rect.bottom:
            self.y += self.settings.ship_speed
        self.rect.y = self.y

    def center_ship(self):
        self.rect.midleft = self.screen_rect.midleft
        self.y = float(self.rect.y)

