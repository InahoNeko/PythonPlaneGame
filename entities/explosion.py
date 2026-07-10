import pygame


class Explosion:

    def __init__(self, x, y):

        self.x = x
        self.y = y

        self.radius = 8

        self.max_radius = 25

        self.speed = 2

        self.alive = True

    def update(self):

        self.radius += self.speed

        if self.radius >= self.max_radius:

            self.alive = False

    def draw(self, screen):

        pygame.draw.circle(

            screen,

            (255, 220, 0),

            (int(self.x), int(self.y)),

            self.radius,

            2

        )

    def die(self):

        self.alive = False