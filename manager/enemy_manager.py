import pygame

from entities.enemy import Enemy
from config.settings import MAX_ENEMY, SPAWN_DELAY


class EnemyManager:

    def __init__(self):

        self.enemies = []
        self.spawn_timer = pygame.time.get_ticks()

    # ======================
    # 更新敌人
    # ======================

    def update(self, player):

        if not player.alive:
            return

        for enemy in self.enemies:

            enemy.move(player)

    # ======================
    # 绘制敌人
    # ======================

    def draw(self, screen):

        for enemy in self.enemies:

            enemy.draw(screen)

    # ======================
    # 创建敌人
    # ======================

    def spawn_enemy(self):

        if len(self.enemies) < MAX_ENEMY:

            self.enemies.append(
                Enemy()
            )



    # ======================
    # 删除敌人
    # ======================

    def remove_dead_enemies(self):

        self.enemies = [

            enemy

            for enemy in self.enemies

            if enemy.alive

        ]

    # ======================
    # 重启
    # ======================

    def restart(self):

        self.enemies = []

    def update_enemy_add(self):

        current_time = pygame.time.get_ticks()

        if current_time - self.spawn_timer >= SPAWN_DELAY:
            self.spawn_enemy()

            self.spawn_timer = current_time