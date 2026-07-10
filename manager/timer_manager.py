import pygame


class TimerManager:

    def __init__(self):

        self.timers = {}

    # ======================
    # 开始计时
    # ======================

    def start(self, name):

        self.timers[name] = pygame.time.get_ticks()

    # ======================
    # 获取经过时间（毫秒）
    # ======================

    def elapsed(self, name):

        if name not in self.timers:
            return 0

        return pygame.time.get_ticks() - self.timers[name]

    # ======================
    # 是否达到指定时间
    # ======================

    def is_timeout(self, name, delay):

        return self.elapsed(name) >= delay

    # ======================
    # 重置计时器
    # ======================

    def reset(self, name):

        self.start(name)

    # ======================
    # 重启
    # ======================

    def restart(self):

        self.timers.clear()