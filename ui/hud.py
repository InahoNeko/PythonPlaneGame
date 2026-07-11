import pygame


class HUD:

    def __init__(self,asset_manager):

        # ======================
        # 字体
        # ======================

        self.font = pygame.font.SysFont(
            None,
            36
        )

        # ======================
        # HUD布局
        # ======================

        self.margin = 15              # 左上边距
        self.score_y = 15             # 分数Y坐标
        self.health_y = 55            # 血量Y坐标

        self.heart_size = 32          # 爱心大小
        self.heart_spacing = 40       # 爱心间距

        # ======================
        # 加载图片
        # ======================

        self.heart_full = asset_manager.get_image(

            "heart_full"

        )

        self.heart_empty = asset_manager.get_image(

            "heart_empty"

        )

        # ======================
        # 缩放图片
        # ======================

        self.heart_full = pygame.transform.scale(

            self.heart_full,

            (

                self.heart_size,

                self.heart_size

            )

        )

        self.heart_empty = pygame.transform.scale(

            self.heart_empty,

            (

                self.heart_size,

                self.heart_size

            )

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

            (

                self.margin,

                self.score_y

            )

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

                image = self.heart_full

            else:

                image = self.heart_empty

            screen.blit(

                image,

                (

                    self.margin + i * self.heart_spacing,

                    self.health_y

                )

            )