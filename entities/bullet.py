from config.settings import BULLET_SPEED, BULLET_WIDTH, BULLET_HEIGHT, WHITE
import pygame


class Bullet:


    def __init__(self,x,y):

        self.trail = []
        self.x=float(x)
        self.y=float(y)


        self.speed = BULLET_SPEED

        self.alive=True

    def move(self):

        self.trail.append(

            (

                self.x + BULLET_WIDTH // 2,

                self.y + BULLET_HEIGHT // 2

            )

        )

        if len(self.trail) > 6:
            self.trail.pop(0)

        self.y -= self.speed

        if self.y < 0:
            self.alive = False

    def draw(self, screen):

        if not self.alive:
            return

        # ======================
        # 绘制拖尾
        # ======================

        trail_count = len(self.trail)

        for index, pos in enumerate(self.trail):
            radius = max(

                1,

                index + 1

            )

            alpha = int(

                255 *

                (

                        index + 1

                )

                /

                max(

                    1,

                    trail_count

                )

            )

            surface = pygame.Surface(

                (

                    radius * 2,

                    radius * 2

                ),

                pygame.SRCALPHA

            )

            pygame.draw.circle(

                surface,

                (

                    120,

                    220,

                    255,

                    alpha

                ),

                (

                    radius,

                    radius

                ),

                radius

            )

            screen.blit(

                surface,

                (

                    pos[0] - radius,

                    pos[1] - radius

                )

            )

        # ======================
        # 绘制子弹
        # ======================

        pygame.draw.rect(

            screen,

            WHITE,

            (

                self.x,

                self.y,

                BULLET_WIDTH,

                BULLET_HEIGHT

            )

        )

    def die(self):
        self.alive=False