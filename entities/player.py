import pygame

from config.settings import *


class Player:

    def __init__(self,asset_manager):

        self.size = PLAYER_SIZE

        self.image_size = PLAYER_IMAGE_SIZE

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

        self.x = WIDTH // 2 - self.size // 2

        self.y = HEIGHT // 2 - self.size // 2

        self.speed = PLAYER_SPEED

        self.color = BLUE

        self.alive = True

        self.max_hp = 3

        self.hp = self.max_hp

        self.invincible = False

        self.invincible_time = 1000

        self.hit_timer = 0

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

        image_x = self.x - (

                self.image_size - self.size

        ) // 2

        image_y = self.y - (

                self.image_size - self.size

        ) // 2

        screen.blit(

            self.image,

            (

                image_x,

                image_y

            )

        )

    def hurt(self):

        if self.invincible:
            return

        self.hp -= 1

        print(f"HP : {self.hp}")

        self.invincible = True

        self.hit_timer = pygame.time.get_ticks()

        if self.hp <= 0:
            self.alive = False

    # ======================
    # 死亡
    # ======================

    def die(self):

        self.hp -= 1

        print(f"HP : {self.hp}")

        if self.hp <= 0:
            self.alive = False