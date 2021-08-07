class Gamestats:
    def __init__(self, shooting):
        self.settings = shooting.settings
        self.reset_stats()

        self.game_active = True

    def reset_stats(self):
        self.ships_left = self.settings.ship_limit
