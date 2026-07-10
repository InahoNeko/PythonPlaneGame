from config import settings
WIDTH = settings.WIDTH
HEIGHT = settings.HEIGHT
from entities.player import Player

class PlayerManager:

    def __init__(self):
        self.player = Player()

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
        self.player = Player()

        self.player.invincible = False

        self.player.hit_timer = 0
