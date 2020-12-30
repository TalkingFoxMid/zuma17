class TaskNormalizeSpace:
    def __init__(self, game_state):
        """Возвращает на место смещения шариков (анимация при выстреле и
        свапе) """
        self.game_state = game_state
        self.remain = 10

    def tick(self):
        if self.remain <= 0:
            self.game_state.time_space_opacity = 0
            return
        self.game_state.time_space_opacity -= 0.1
        self.remain -= 1

    def get_remain(self):
        return self.remain
