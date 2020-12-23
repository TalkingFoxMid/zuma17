class TaskResetParameter:
    def __init__(self, game_state,
                 is_reset_shot_swap,
                 is_reset_swap_swap,
                 is_reset_change_swap = False):
        self.remain = 5
        self.is_reset_shot_swap = is_reset_shot_swap
        self.is_reset_swap_swap = is_reset_swap_swap
        self.is_reset_change_swap = is_reset_change_swap
        self.game_state = game_state
    def tick(self):
        p1 = self.game_state.balls_swap_parameter
        p2 = self.game_state.balls_swap_parameter2
        p3 = self.game_state.balls_swap_parameter3

        if self.is_reset_shot_swap:
            self.game_state.balls_swap_parameter -= 0.2

        if self.is_reset_swap_swap:
            self.game_state.balls_swap_parameter2 -= 0.2

        if self.is_reset_change_swap:
            self.game_state.balls_swap_parameter3 -= 0.2

        self.remain -= 1
        if self.remain <= 0:
            self.game_state.balls_swap_parameter = 0
            self.game_state.balls_swap_parameter2 = 0
            self.game_state.balls_swap_parameter3 = 0
            return
    def get_remain(self):
        return self.remain