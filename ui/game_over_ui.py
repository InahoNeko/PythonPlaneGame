import pygame

class GameOverUI:

    def __init__(self):

        self.font = pygame.font.SysFont(
            None,
            60
        )

        self.small_font = pygame.font.SysFont(
            None,
            35
        )

    def draw(self, screen):
        text = self.font.render(

            "GAME OVER",

            True,

            (255, 0, 0)

        )

        text_rect = text.get_rect(

            center=(

                screen.get_width() // 2,

                screen.get_height() // 2 - 30

            )

        )

        screen.blit(

            text,

            text_rect

        )

        restart = self.small_font.render(

            "Press R to Restart",

            True,

            (255, 255, 255)

        )

        restart_rect = restart.get_rect(

            center=(

                screen.get_width() // 2,

                screen.get_height() // 2 + 30

            )

        )

        screen.blit(

            restart,

            restart_rect

        )