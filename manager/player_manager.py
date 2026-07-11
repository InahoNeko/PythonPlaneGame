from config import settings
WIDTH = settings.WIDTH
HEIGHT = settings.HEIGHT
from entities.player import Player

class PlayerManager:

    def __init__(self,asset_manager):
        self.player = Player(asset_manager)
        self.asset_manager = asset_manager

    def update(self, keys):
        if not self.player.alive:
            return

        self.player.move(keys)

        self.player.boundary(
            WIDTH,
            HEIGHT
        )

    def draw(self, screen):
        self.player.draw(screen)

    def restart(self):
        self.player = Player(self.asset_manager)

        self.player.invincible = False

        self.player.hit_timer = 0
