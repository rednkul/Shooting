from random import randrange


class Settings:

    def __init__(self):
        self.ship_speed = 1

        self.bullets_limit = 3
        self.bullet_speed = 1

        self.bullet_width = 50
        self.bullet_height = 200
        self.bullet_color = (130, 130, 130)

        self.cub_color = (255, 0, 0)
        self.cub_speed = 0
        self.cub_width = 40
        self.cub_height = 40
        self.direction = randrange(-1, 2, 2)
