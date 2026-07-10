class CollisionSystem:

    def __init__(
        self,
        player_manager,
        enemy_manager,
        bullet_manager,
        score_manager,
        effect_manager,
        sound_manager
    ):

        self.player_manager = player_manager

        self.enemy_manager = enemy_manager

        self.bullet_manager = bullet_manager

        self.score_manager = score_manager

        self.effect_manager = effect_manager

        self.sound_manager = sound_manager

    def bullet_hit_enemy(self, enemy):
        if not enemy.alive:
            return

        for bullet in self.bullet_manager.bullets:

            if (

                bullet.x < enemy.x + enemy.size

                and

                bullet.x + 5 > enemy.x

                and

                bullet.y < enemy.y + enemy.size

                and

                bullet.y + 5 > enemy.y

            ):

                enemy.die()


                bullet.die()

                print("击中敌人！")

                self.score_manager.add_score()
                print(f"当前分数：{self.score_manager.get_score()}")

                self.effect_manager.create_explosion(

                    enemy.x + enemy.size // 2,

                    enemy.y + enemy.size // 2

                )

                self.sound_manager.play("explosion")

                return

    def check_bullet_collision(self):

        if not self.player_manager.player.alive:
            return

        for enemy in self.enemy_manager.enemies:

            self.bullet_hit_enemy(enemy)

        # ======================
        # 玩家碰撞敌人
        # ======================

    def check_player_enemy_collision(self):

        if not self.player_manager.player.alive:
            return

        for enemy in self.enemy_manager.enemies:

            if not enemy.alive:
                continue

            if (

                    self.player_manager.player.x <
                    enemy.x + enemy.size

                    and

                    self.player_manager.player.x
                    + self.player_manager.player.size >
                    enemy.x

                    and

                    self.player_manager.player.y <
                    enemy.y + enemy.size

                    and

                    self.player_manager.player.y
                    + self.player_manager.player.size >
                    enemy.y

            ):
                print("碰到了！")

                self.player_manager.player.hurt()

                self.sound_manager.play("player_die")

                return

    def update(self):
        self.check_bullet_collision()

        self.check_player_enemy_collision()