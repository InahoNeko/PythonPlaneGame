import pygame


class HUD:

    def __init__(self):

        self.font = pygame.font.SysFont(
            None,
            36
        )

    def draw(self, screen, score_manager):

        text = self.font.render(

            f"Score : {score_manager.get_score()}",

            True,

            (255, 255, 255)

        )

        screen.blit(

            text,

            (15, 15)

        )