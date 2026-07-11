import pygame


class BackgroundManager:

    def __init__(self, asset_manager):

        # 获取背景图片
        self.background = asset_manager.get_image("background")

        # 两张背景的位置
        self.y1 = 0
        self.y2 = -self.background.get_height()

        # 滚动速度（以后放 settings.py）
        self.speed = 2

    # ======================
    # 更新
    # ======================

    def update(self):

        self.y1 += self.speed
        self.y2 += self.speed

        height = self.background.get_height()

        if self.y1 >= height:
            self.y1 = self.y2 - height

        if self.y2 >= height:
            self.y2 = self.y1 - height

    # ======================
    # 绘制
    # ======================

    def draw(self, screen):

        screen.blit(
            self.background,
            (0, self.y1)
        )

        screen.blit(
            self.background,
            (0, self.y2)
        )

    # ======================
    # 重置
    # ======================

    def restart(self):

        self.y1 = 0
        self.y2 = -self.background.get_height()