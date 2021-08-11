class Gamestats:
    def __init__(self, shooting):
        self.settings = shooting.settings
        self.reset_stats()

        self.game_active = False

    def reset_stats(self):
        """Сброс статистики игры"""
        self.ships_left = self.settings.ship_limit
