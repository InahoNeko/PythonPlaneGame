import pygame

from config.settings import *


class Player:

    def __init__(self):

        self.size = PLAYER_SIZE

        self.x = WIDTH // 2 - self.size // 2

        self.y = HEIGHT // 2 - self.size // 2

        self.speed = PLAYER_SPEED

        self.color = BLUE

        self.alive = True

    # ======================
    # 移动
    # ======================

    def move(self, keys):

        if keys[pygame.K_a]:

            self.x -= self.speed

        if keys[pygame.K_d]:

            self.x += self.speed

        if keys[pygame.K_w]:

            self.y -= self.speed

        if keys[pygame.K_s]:

            self.y += self.speed

    # ======================
    # 边界检测
    # ======================

    def boundary(self, width, height):

        if self.x < 0:

            self.x = 0

        if self.x > width - self.size:

            self.x = width - self.size

        if self.y < 0:

            self.y = 0

        if self.y > height - self.size:

            self.y = height - self.size

    # ======================
    # 绘制
    # ======================

    def draw(self, screen):

        if not self.alive:
            return

        pygame.draw.rect(

            screen,

            self.color,

            (
                self.x,
                self.y,
                self.size,
                self.size
            )

        )

    # ======================
    # 死亡
    # ======================

    def die(self):

        self.alive = False