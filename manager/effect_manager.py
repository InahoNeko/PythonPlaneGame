from entities.explosion import Explosion


class EffectManager:

    def __init__(self):

        self.effects = []

    # ======================
    # 创建爆炸
    # ======================

    def create_explosion(self, x, y):

        self.effects.append(

            Explosion(x, y)

        )

    # ======================
    # 更新
    # ======================

    def update(self):

        for effect in self.effects:

            effect.update()

        self.remove_dead_effects()

    # ======================
    # 绘制
    # ======================

    def draw(self, screen):

        for effect in self.effects:

            effect.draw(screen)

    # ======================
    # 删除
    # ======================

    def remove_dead_effects(self):

        self.effects = [

            effect

            for effect in self.effects

            if effect.alive

        ]

    # ======================
    # 重启
    # ======================

    def restart(self):

        self.effects.clear()