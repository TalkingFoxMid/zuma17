from flyingBall import FlyingBall
from random_color_manager import RandomColorManager
from task_reset_parameter import TaskResetParameter


class FrogOperator:
    def __init__(self, game_state):
        self.gs = game_state
        self.balls_swap_parameter = 0
        self.balls_swap_parameter2 = 0
        self.balls_swap_parameter3 = 0
        self.random_color_manager = RandomColorManager()
        self.first_ball_color = 'red'
        self.second_ball_color = 'red'
        self.third_ball_color = 'red'
        self.change_balls_cooldown = 0
        self.cooldown = 0

    def is_cool_down(self):
        return self.cooldown > 0

    def down_cooldowns(self):
        if self.cooldown > 0:
            self.cooldown -= 1
        if self.change_balls_cooldown > 0:
            self.change_balls_cooldown -= 1

    def freeze_cooldown(self):
        self.cooldown = 5

    def freeze_change_cooldown(self):
        self.change_balls_cooldown = 250

    def shot_a_ball(self, angle):
        if self.cooldown > 0:
            return
        self.freeze_cooldown()
        self.balls_swap_parameter = 1
        self.gs.add_task(TaskResetParameter(self.gs, True, False))
        clr = self.first_ball_color
        self.first_ball_color = self.second_ball_color
        self.second_ball_color = self.third_ball_color
        self.third_ball_color = self.random_color_manager.get_random_color(
            self.gs.balls_conveyor.get_color_distribution()
        )

        self.gs.balls.append(FlyingBall(angle=angle,
                                        color=clr))

    def swap_balls(self):
        if self.cooldown > 0:
            return
        self.freeze_cooldown()
        tmp = self.first_ball_color
        self.first_ball_color = self.second_ball_color
        self.second_ball_color = self.third_ball_color
        self.third_ball_color = tmp
        self.balls_swap_parameter = 1
        self.balls_swap_parameter2 = 1

        self.gs.add_task(TaskResetParameter(self.gs, True, True))

    def change_balls(self):
        if self.change_balls_cooldown > 0:
            return
        self.freeze_change_cooldown()
        self.balls_swap_parameter3 = 1
        self.first_ball_color = self.random_color_manager.get_random_color(
            self.gs.balls_conveyor.get_color_distribution()
        )
        self.second_ball_color = self.random_color_manager.get_random_color(
            self.gs.balls_conveyor.get_color_distribution()
        )
        self.third_ball_color = self.random_color_manager.get_random_color(
            self.gs.balls_conveyor.get_color_distribution()
        )
        self.gs.add_task(
            TaskResetParameter(
                self.gs,
                False,
                False,
                True
            )
        )
