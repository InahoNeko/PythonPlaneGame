import random

import pygame


class CameraManager:

    def __init__(self):

        self.offset_x = 0
        self.offset_y = 0

        # ======================
        # Screen Shake
        # ======================

        self.shake_intensity = 0

        self.shake_duration = 0

        self.shake_start_time = 0

        self.shaking = False

    # ======================
    # 开始震动
    # ======================

    def shake(self, intensity, duration):

        self.shake_intensity = intensity

        self.shake_duration = duration

        self.shake_start_time = pygame.time.get_ticks()

        self.shaking = True



    # ======================
    # 更新
    # ======================

    # ======================
    # 更新
    # ======================

    def update(self):

        if not self.shaking:
            self.offset_x = 0

            self.offset_y = 0

            return

        current_time = pygame.time.get_ticks()

        elapsed = current_time - self.shake_start_time

        if elapsed >= self.shake_duration:
            self.offset_x = 0

            self.offset_y = 0

            self.shaking = False

            return

        # ======================
        # 计算剩余强度（线性衰减）
        # ======================

        ratio = 1 - elapsed / self.shake_duration

        current_intensity = self.shake_intensity * ratio

        # ======================
        # 随机偏移
        # ======================

        self.offset_x = random.randint(

            -int(current_intensity),

            int(current_intensity)

        )

        self.offset_y = random.randint(

            -int(current_intensity),

            int(current_intensity)

        )

    # ======================
    # 获取偏移
    # ======================

    def get_offset(self):

        return (

            self.offset_x,

            self.offset_y

        )

    # ======================
    # 重置
    # ======================

    def reset(self):

        self.offset_x = 0

        self.offset_y = 0

        self.shaking = False