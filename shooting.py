import sys
import pygame

from settings import Settings
from cube import Cube
from ship import Ship
from bullet import Bullet
from gamestats import Gamestats
from button import Button



class Shooting:
    """Инициализация компонентов игры"""
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.stats = Gamestats(self)
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.ship = Ship(self)
        self.cube = Cube(self)
        self.bullets = pygame.sprite.Group()
        self.playbutton = Button(self, 'Play')

        pygame.display.set_caption("Shooting trainer")


    def run_game(self):
        while True:

            self._check_events()
            if self.stats.game_active:
                self._update_bullets()
                self.ship.update_ship()
                self._update_cube()
            self._update_screen()



    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_playbutton(mouse_pos)

    def _check_keydown_events(self,event):
        if event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_p:
            self.start_game()


    def _check_keyup_events(self,event):
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _check_playbutton(self, mouse_pos):
        button_cliked = self.playbutton.rect.collidepoint(mouse_pos)
        if button_cliked:
            self.start_game()

    def start_game(self):
        """Запускает игру"""
        if not self.stats.game_active:
            # Сброс игровой статистики
            self.stats.reset_stats()
            self.stats.game_active = True

            # Очистка списков пришельцев и снарядов
            self.bullets.empty()

            # Размещение корабля и куба в центре
            self.ship.center_ship()
            self.cube.center_cube()

        # Сокрытие указателя мыши
        pygame.mouse.set_visible(False)

        self.settings.initialize_dynamic_settings()


    def _fire_bullet(self):
        """Создание нового снаряда и включение его в группу bullets."""
        new_bullet = Bullet(self)
        if len(self.bullets) < self.settings.bullets_limit:
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Обновляет позицию снаряда и удаляет его при уходе за экран"""
        # Обновление позиции снаряда .
        self.bullets.update()
        self._check_miss()
        self._chek_bullet_cube_collisions()

    def _check_miss(self):
        for bullet in self.bullets.copy():
            if bullet.rect.left >= self.screen.get_rect().right:
                if self.stats.ships_left:
                    self.bullets.remove(bullet)
                    self.stats.ships_left -= 1
                else:
                    self.stats.game_active = False

    def _update_cube(self):
        self.cube.cub_update()
        self._check_cub_edges()

    def _check_cub_edges(self):
        if self.cube.check_edges():
            self._change_direction()


    def _change_direction(self):
        self.settings.direction *= -1

    def _chek_bullet_cube_collisions(self):
        collision = pygame.sprite.spritecollide(self.cube, self.bullets, True)
        if collision:
            self.settings.increase_speed()

    def _update_screen(self):

        self.screen.fill((0, 0, 0))
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.cube.draw_cube()

        # Кнопка Play отображается только если игра не активна
        if not self.stats.game_active:
            self.playbutton.draw_button()


        pygame.display.flip()


if __name__ == '__main__':
    shooting = Shooting()
    shooting.run_game()