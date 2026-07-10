import pygame


class SoundManager:

    def __init__(self):

        self.sounds = {}

    # ======================
    # 加载音效
    # ======================

    def load(self, name, path):

        self.sounds[name] = pygame.mixer.Sound(path)

    # ======================
    # 播放音效
    # ======================

    def play(self, name):

        sound = self.sounds.get(name)

        if sound:

            sound.play()

    # ======================
    # 设置音量
    # ======================

    def set_volume(self, name, volume):

        sound = self.sounds.get(name)

        if sound:

            sound.set_volume(volume)