import pygame


class HUD:

    def __init__(self):

        self.font = pygame.font.SysFont(
            None,
            36
        )

        # ======================
        # 加载爱心图片
        # ======================

        self.heart_full = pygame.image.load(
            "assets/images/ui/heart_full.png"
        ).convert_alpha()

        self.heart_empty = pygame.image.load(
            "assets/images/ui/heart_empty.png"
        ).convert_alpha()

        # 缩放到 32×32
        self.heart_full = pygame.transform.scale(
            self.heart_full,
            (32, 32)
        )

        self.heart_empty = pygame.transform.scale(
            self.heart_empty,
            (32, 32)
        )

    # ======================
    # 绘制HUD
    # ======================

    def draw(
            self,
            screen,
            score_manager,
            player
    ):

        self.draw_score(

            screen,

            score_manager

        )

        self.draw_health(

            screen,

            player

        )

    # ======================
    # 绘制分数
    # ======================

    def draw_score(
            self,
            screen,
            score_manager
    ):

        text = self.font.render(

            f"Score : {score_manager.get_score()}",

            True,

            (255, 255, 255)

        )

        screen.blit(

            text,

            (15, 15)

        )

    # ======================
    # 绘制生命值
    # ======================

    def draw_health(
            self,
            screen,
            player
    ):

        for i in range(player.max_hp):

            if i < player.hp:

                screen.blit(

                    self.heart_full,

                    (

                        15 + i * 40,

                        55

                    )

                )

            else:

                screen.blit(

                    self.heart_empty,

                    (

                        15 + i * 40,

                        55

                    )

                )