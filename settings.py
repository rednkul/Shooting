from random import randrange


class Settings:
    """Класс настроек"""

    def __init__(self):
        """Инициализирует статические настрйоки"""
        # Количество жизней
        self.ship_limit = 3

        # Количество снарядов
        self.bullets_limit = 5

        # Характеристики снаряда
        self.bullet_width = 20
        self.bullet_height = 5
        self.bullet_color = (250, 130, 130)

        # Характеристики мишени
        self.cub_color = (255, 0, 0)
        self.cub_width = 40
        self.cub_height = 40

        # Начальное направление движения мишени
        self.direction = randrange(-1, 2, 2)

        # Значение прироста скорости игры
        self.speedup_scale = 1.05

        # Иницализирует изменяющиеся в ходе игры настройки
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Настройки скорости игры"""
        self.ship_speed = 1
        self.bullet_speed = 1
        self.cub_speed = 1

    def increase_speed(self):
        """Прирост скорости игры"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.cub_speed *= self.speedup_scale