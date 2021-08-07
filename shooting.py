import sys
import pygame

from settings import Settings
from cube import Cube
from ship import Ship
from bullet import Bullet


class Shooting:
    """Инициализация компонентов игры"""
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((1000,1000))
        self.ship = Ship(self)
        self.cube = Cube(self)
        self.bullets = pygame.sprite.Group()

        pygame.display.set_caption("Shooting trainer")


    def run_game(self):
        while True:
            self._check_events()
            self._update_bullets()
            self._update_screen()
            self.ship.update_ship()
            self._update_cube()



    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self,event):
        if event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_q:
            sys.exit()


    def _check_keyup_events(self,event):
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _fire_bullet(self):
        """Создание нового снаряда и включение его в группу bullets."""
        new_bullet = Bullet(self)
        if len(self.bullets) < self.settings.bullets_limit:
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Обновляет позицию снаряда и удаляет его при уходе за экран"""
        # Обновление позиции снаряда .
        self.bullets.update()

        # Удаление снаряда, вышедшего за край экрана.
        for bullet in self.bullets.copy():
            if bullet.rect.left >= self.screen.get_rect().right:
                self.bullets.remove(bullet)

    def _update_cube(self):
        self.cube.cub_update()
        self._check_cub_edges()

    def _check_cub_edges(self):
        if self.cube.check_edges():
            self._change_direction()


    def _change_direction(self):
        self.settings.direction *= -1

    def _update_screen(self):

        self.screen.fill((0, 0, 0))
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.cube.draw_cube()


        pygame.display.flip()


if __name__ == '__main__':
    shooting = Shooting()
    shooting.run_game()