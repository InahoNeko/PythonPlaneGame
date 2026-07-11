import pygame
import math

from config.settings import *


class Player:

    def __init__(self,asset_manager):

        self.engine_time = 0

        self.engine_scale = 1.0

        self.size = PLAYER_SIZE

        self.image_size = PLAYER_IMAGE_SIZE

        self.image = asset_manager.get_image(

            "player"

        )

        self.image = pygame.transform.scale(

            self.image,

            (

                self.image_size,

                self.image_size

            )

        )

        # ======================
        # 尾焰
        # ======================

        self.engine_size = PLAYER_IMAGE_SIZE // 2

        self.engine_image = asset_manager.get_image(

            "engine"

        )

        self.engine_image = pygame.transform.scale(

            self.engine_image,

            (

                self.engine_size,

                self.engine_size

            )

        )

        self.x = WIDTH // 2 - self.size // 2

        self.y = HEIGHT // 2 - self.size // 2

        self.speed = PLAYER_SPEED

        self.color = BLUE

        self.alive = True

        self.max_hp = 3

        self.hp = self.max_hp

        self.invincible = False

        self.hit_timer = 0

        self.invincible_time = 800  # 毫秒

        self.flash_interval = 100  # 每100毫秒闪一次

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

        if self.invincible:

            if pygame.time.get_ticks() - self.hit_timer >= self.invincible_time:
                self.invincible = False

        self.engine_time += 0.18

        self.engine_scale = 1 + math.sin(
            self.engine_time
        ) * 0.08

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

    def draw_engine(

            self,

            screen,

            image_x,

            image_y

    ):

        # 当前尾焰高度
        current_height = int(

            self.engine_size *

            self.engine_scale

        )

        # 呼吸缩放（只拉伸高度）
        engine_image = pygame.transform.smoothscale(

            self.engine_image,

            (

                self.engine_size,

                current_height

            )

        )

        # X 保持居中
        engine_x = image_x + (

                self.image_size -

                self.engine_size

        ) // 2

        # 固定喷口位置
        engine_y = (

                image_y +

                self.image_size -

                8 -

                (

                        current_height -

                        self.engine_size

                )

        )

        screen.blit(

            engine_image,

            (

                engine_x,

                engine_y

            )

        )

    def draw(self, screen):

        if not self.alive:
            return

        if self.invincible:

            current_time = pygame.time.get_ticks()

            if (current_time // self.flash_interval) % 2 == 0:
                return

        image_x = self.x - (

                self.image_size - self.size

        ) // 2

        image_y = self.y - (

                self.image_size - self.size

        ) // 2

        self.draw_engine(

            screen,

            image_x,

            image_y

        )

        screen.blit(

            self.image,

            (

                image_x,

                image_y

            )

        )

    def take_damage(self):

        if self.invincible:
            return

        self.hp -= 1

        print(f"HP : {self.hp}")

        self.invincible = True

        self.hit_timer = pygame.time.get_ticks()

        if self.hp <= 0:
            self.die()

    # ======================
    # 死亡
    # ======================

    def die(self):


            self.alive = False