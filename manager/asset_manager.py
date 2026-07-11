import pygame


class AssetManager:

    def __init__(self):

        self.images = {}

        self.sounds = {}

    # ======================
    # 加载图片
    # ======================

    def load_image(

            self,

            name,

            path

    ):

        self.images[name] = pygame.image.load(

            path

        ).convert_alpha()

    # ======================
    # 获取图片
    # ======================

    def get_image(

            self,

            name

    ):

        return self.images[name]

    # ======================
    # 加载音效
    # ======================

    def load_sound(

            self,

            name,

            path

    ):

        self.sounds[name] = pygame.mixer.Sound(

            path

        )

    # ======================
    # 获取音效
    # ======================

    def get_sound(

            self,

            name

    ):

        return self.sounds[name]