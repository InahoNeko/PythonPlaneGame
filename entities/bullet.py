from config.settings import BULLET_SPEED, BULLET_WIDTH, BULLET_HEIGHT, WHITE
import pygame


class Bullet:


    def __init__(self,x,y):

        self.x=x

        self.y=y

        self.speed = BULLET_SPEED

        self.alive=True



    def move(self):

        self.y -= self.speed


        if self.y < 0:

            self.alive=False



    def draw(self,screen):

        if self.alive:

            pygame.draw.rect(
                screen,
                WHITE,
                (
                    self.x,
                    self.y,BULLET_WIDTH,BULLET_HEIGHT
                )
            )

    def die(self):
        self.alive=False