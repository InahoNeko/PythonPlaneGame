from entities.bullet import Bullet
import pygame

class BulletManager:

    def __init__(self,sound_manager):

        self.bullets = []

        self.can_shoot = True

        self.sound_manager = sound_manager

    # ======================
    # 更新子弹
    # ======================

    def update(self):

        for bullet in self.bullets:

            bullet.move()

    # ======================
    # 射击
    # ======================

    def update_shooting(self, keys, player):

        if not player.alive:
            return

        if (

            keys[pygame.K_SPACE]

            and

            self.can_shoot

        ):

            self.bullets.append(

                Bullet(

                    player.x
                    + player.size // 2
                    - 2,

                    player.y

                )

            )

            self.sound_manager.play("shoot")

            self.can_shoot = False

        if not keys[pygame.K_SPACE]:

            self.can_shoot = True

    # ======================
    # 绘制子弹
    # ======================

    def draw(self, screen):

        for bullet in self.bullets:

            bullet.draw(screen)

    # ======================
    # 删除死亡子弹
    # ======================

    def remove_dead_bullets(self):

        self.bullets = [

            bullet

            for bullet in self.bullets

            if bullet.alive

        ]

    # ======================
    # 重启
    # ======================

    def restart(self):

        self.bullets = []

        self.can_shoot = True