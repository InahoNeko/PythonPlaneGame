import pygame
from entities.enemy import Enemy
from config.settings import MAX_ENEMY, SPAWN_DELAY
from manager.timer_manager import TimerManager


class EnemyManager:

    def __init__(self,asset_manager):

        self.asset_manager = asset_manager

        self.enemies = []

        self.spawn_timer = pygame.time.get_ticks()

        self.timer_manager = TimerManager()

        self.timer_manager.start("spawn")

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

                Enemy(self.asset_manager)

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
    # 更新敌人生成
    # ======================

    def update_enemy_add(self):

        if self.timer_manager.is_timeout(

            "spawn",

            SPAWN_DELAY

        ):

            self.spawn_enemy()

            self.timer_manager.reset("spawn")

    # ======================
    # 重启
    # ======================

    def restart(self):

        self.enemies = []

        self.timer_manager.restart()

        self.timer_manager.start("spawn")