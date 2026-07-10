import pygame



class HealthUI:

    def __init__(self):

        self.font = pygame.font.SysFont(
            None,
            36
        )

        self.heart_full = pygame.image.load(
            "assets/images/ui/heart_full.png"
        ).convert_alpha()

        self.heart_empty = pygame.image.load(
            "assets/images/ui/heart_empty.png"
        ).convert_alpha()

        self.heart_full = pygame.transform.scale(
            self.heart_full,
            (32, 32)
        )

        self.heart_empty = pygame.transform.scale(
            self.heart_empty,
            (32, 32)
        )

    def draw(self, screen, player):

        for i in range(player.max_hp):

            if i < player.hp:

                screen.blit(

                    self.heart_full,

                    (

                        20 + i * 40,

                        20

                    )

                )

            else:

                screen.blit(

                    self.heart_empty,

                    (

                        20 + i * 40,

                        20

                    )

                )