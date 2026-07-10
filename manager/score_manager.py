class ScoreManager:

    def __init__(self):

        self.score = 0

    # ======================
    # 增加分数
    # ======================

    def add_score(self, value=1):

        self.score += value

    # ======================
    # 获取分数
    # ======================

    def get_score(self):

        return self.score

    # ======================
    # 重置
    # ======================

    def restart(self):

        self.score = 0