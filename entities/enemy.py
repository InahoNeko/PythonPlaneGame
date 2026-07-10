from config.settings import ENEMY_SIZE, ENEMY_SPEED,WIDTH,HEIGHT,RED
import pygame
import random
import math

class Enemy:


    def __init__(self):

        self.x = random.randint(
            0,
            WIDTH-20
        )

        self.y = HEIGHT // 4.5

        self.size = ENEMY_SIZE
        self.speed = ENEMY_SPEED


        self.alive = True



    def move(self, player):

        if not self.alive:
            return


        dx = player.x - self.x

        dy = player.y - self.y


        distance = math.sqrt(
            dx * dx +
            dy * dy
        )


        if distance != 0:

            self.x += (
                dx / distance *
                self.speed
            )

            self.y += (
                dy / distance *
                self.speed
            )



    def draw(self,screen):

        if self.alive:

            pygame.draw.rect(
                screen,
                RED,
                (
                    self.x,
                    self.y,
                    self.size,
                    self.size
                )
            )



    def die(self):


        self.alive=False