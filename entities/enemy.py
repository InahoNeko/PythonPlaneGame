from config.settings import *
import pygame
import random
import math

class Enemy:


    def __init__(self,asset_manager):

        self.image_size = ENEMY_IMAGE_SIZE

        self.image = asset_manager.get_image(

            "enemy"

        )

        self.image = pygame.transform.scale(

            self.image,

            (

                self.image_size,

                self.image_size

            )

        )

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



    def die(self):


        self.alive=False