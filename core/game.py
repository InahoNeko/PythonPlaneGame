import pygame

from manager.background_manager import BackgroundManager
from manager.player_manager import PlayerManager
from manager.enemy_manager import EnemyManager
from manager.bullet_manager import BulletManager
from core.collision_system import CollisionSystem
from manager.score_manager import ScoreManager
from manager.effect_manager import EffectManager
from manager.sound_manager import SoundManager
from manager.asset_manager import AssetManager

from core.game_state import GameState
from ui.ui_manager import UIManager



class Game:

    def __init__(self):

        self.asset_manager = AssetManager()

        self.sound_manager = SoundManager()

        # 先加载资源
        self.load_assets()
        self.load_sounds()
        self.background_manager = BackgroundManager(
            self.asset_manager
        )

        # 再创建需要资源的对象
        self.player_manager = PlayerManager(self.asset_manager)
        self.enemies_manager = EnemyManager(self.asset_manager)
        self.bullet_manager = BulletManager(self.sound_manager)

        self.score_manager = ScoreManager()
        self.effect_manager = EffectManager()

        self.collision_system = CollisionSystem(
            self.player_manager,
            self.enemies_manager,
            self.bullet_manager,
            self.score_manager,
            self.effect_manager,
            self.sound_manager
        )

        self.game_state = GameState()

        self.ui_manager = UIManager(self.asset_manager)
    # ======================
    # 加载声音
    # ======================

    def load_sounds(self):

        self.sound_manager.load(
            "shoot",
            "assets/sounds/shoot.wav"
        )

        self.sound_manager.load(
            "explosion",
            "assets/sounds/explosion.wav"
        )

        self.sound_manager.load(
            "player_die",
            "assets/sounds/player_die.wav"
        )

    # ======================
    # 加载图片
    # ======================

    def load_assets(self):

        self.asset_manager.load_image(

            "background",

            "assets/images/background/background.png"

        )

        self.asset_manager.load_image(

            "heart_full",

            "assets/images/ui/heart_full.png"

        )

        self.asset_manager.load_image(

            "heart_empty",

            "assets/images/ui/heart_empty.png"

        )

        # ======================
        # 玩家
        # ======================

        self.asset_manager.load_image(

            "player",

            "assets/images/player/player.png"

        )

        # ======================
        # 敌人
        # ======================

        self.asset_manager.load_image(

            "enemy",

            "assets/images/enemy/enemy.png"

        )
    # ======================
    # 更新游戏
    # ======================

    def update(self, keys):

        if self.game_state.is_playing():

            self.background_manager.update()

            self.player_manager.update(keys)

            self.enemies_manager.update(self.player_manager.player)

            self.bullet_manager.update_shooting(keys,self.player_manager.player)

            self.bullet_manager.update()

            self.collision_system.update()

            self.effect_manager.update()

            self.bullet_manager.remove_dead_bullets()

            self.enemies_manager.remove_dead_enemies()

            self.enemies_manager.update_enemy_add()

            if not self.player_manager.player.alive:
                self.enemies_manager.restart()

                self.bullet_manager.restart()

                self.game_state.game_over()

        self.check_restart(keys)


    # ======================
    # 绘制
    # ======================

    def draw(self, screen):

        self.background_manager.draw(screen)

        self.player_manager.draw(screen)

        self.enemies_manager.draw(screen)

        self.bullet_manager.draw(screen)

        self.effect_manager.draw(screen)

        self.ui_manager.draw(

            screen,

            self.game_state,

            self.score_manager,

            self.player_manager.player

        )


    # ======================
    # 重启
    # ======================

    def restart(self):

        self.player_manager.restart()

        self.enemies_manager.restart()

        self.bullet_manager.restart()

        self.score_manager.restart()


        self.effect_manager.restart()

    def check_restart(self,keys):
        if self.game_state.is_game_over():

            if keys[pygame.K_r]:
                self.restart()

                self.game_state.restart()