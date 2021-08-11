from random import randrange


class Settings:

    def __init__(self):

        self.ship_limit = 3

        self.bullets_limit = 5

        self.bullet_width = 20
        self.bullet_height = 5
        self.bullet_color = (250, 130, 130)

        self.cub_color = (255, 0, 0)
        self.cub_width = 40
        self.cub_height = 40
        self.direction = randrange(-1, 2, 2)

        self.speedup_scale = 1.05

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed = 1
        self.bullet_speed = 1
        self.cub_speed = 1

    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.cub_speed *= self.speedup_scale