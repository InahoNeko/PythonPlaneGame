from ui.game_over_ui import GameOverUI
from ui.hud import HUD
from ui.health_ui import HealthUI


class UIManager:

    def __init__(self):

        self.game_over_ui = GameOverUI()
        self.hud = HUD()
        self.health_ui = HealthUI()

    def draw(
            self,
            screen,
            game_state,
            score_manager,
            player
    ):
        self.hud.draw(
            screen,
            score_manager,
            player
        )

        if game_state.is_game_over():
            self.game_over_ui.draw(screen)