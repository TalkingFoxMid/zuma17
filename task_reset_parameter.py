class TaskResetParameter:
    def __init__(self, game_state, is_reset_shot_swap, is_reset_swap_swap):
        self.remain = 10
        self.is_reset_shot_swap = is_reset_shot_swap
        self.is_reset_swap_swap = is_reset_swap_swap

        self.game_state = game_state
    def tick(self):

        if self.is_reset_shot_swap:
            self.game_state.balls_swap_parameter -= 0.1
        if self.is_reset_swap_swap:
            self.game_state.balls_swap_parameter2 -= 0.1
        self.remain -= 1
        if self.remain <= 0:
            self.game_state.balls_swap_parameter = 0
            self.game_state.balls_show_parameter = 0
            print("RESETED")
            return
    def get_remain(self):
        return self.remain