from ui.game_over_ui import GameOverUI
from ui.hud import HUD


class UIManager:

    def __init__(self):

        self.game_over_ui = GameOverUI()
        self.hud = HUD()

    def draw(
            self,
            screen,
            game_state,
            score_manager
    ):
        self.hud.draw(
            screen,
            score_manager
        )

        if game_state.is_game_over():
            self.game_over_ui.draw(screen)