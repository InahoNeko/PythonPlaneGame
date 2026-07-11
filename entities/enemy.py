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
        self.angle = 0


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

        self.angle = math.degrees(

            math.atan2(

                dy,

                dx

            )

        ) + 90

    def draw(self, screen):

        if not self.alive:
            return

        rotated_image = pygame.transform.rotate(

            self.image,

            -self.angle

        )

        rect = rotated_image.get_rect(

            center=(

                self.x + self.size // 2,

                self.y + self.size // 2

            )

        )

        screen.blit(

            rotated_image,

            rect

        )



    def die(self):


        self.alive=False