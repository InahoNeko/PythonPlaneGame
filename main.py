import pygame

from core.game import Game
from config.settings import *


def main():

    pygame.init()
    pygame.mixer.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption(TITLE)

    clock = pygame.time.Clock()

    game = Game()


    running = True

    while running:

        # ======================
        # 事件
        # ======================

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()

        screen.fill(BLACK)

        # ======================
        # 游戏进行中
        # ======================

        game.update(keys)

        game.draw(screen)

        pygame.display.flip()

        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()