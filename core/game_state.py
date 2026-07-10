class GameState:
    PLAYING = "PLAYING"

    GAME_OVER = "GAME_OVER"

    def __init__(self):
        self.state = self.PLAYING

    def is_playing(self):
        return self.state == self.PLAYING

    def is_game_over(self):
        return self.state == self.GAME_OVER

    def game_over(self):
        self.state = self.GAME_OVER

    def restart(self):
        self.state = self.PLAYING


