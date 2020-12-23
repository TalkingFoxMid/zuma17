from balls_conveyor import BallsConveyor
from task_manager import TaskManager


class GameState:
    def __init__(self, game_level):
        self.angle = 0
        self.animation_manager = None
        self.game_level = game_level
        self.balls_conveyor = BallsConveyor(self, game_level)
        self.balls = []
        self.task_manager = TaskManager()
        self.first_ball_color = 'red'
        self.second_ball_color = 'red'
        self.third_ball_color = 'red'
        self.balls_swap_parameter = 0
        self.balls_swap_parameter2 = 0
        self.balls_swap_parameter3 = 0
        self.score = 0
        self.change_balls_cooldown = 0
        self.cooldown = 0
        self.lost = False
        self.game_ended_win = False

    def set_animation_manager(self, animation_manager):
        self.animation_manager = animation_manager

    def is_cool_down(self):
        return self.cooldown > 0

    def get_angle(self):
        return self.angle

    def down_cooldowns(self):
        if self.cooldown > 0:
            self.cooldown -= 1
        if self.change_balls_cooldown > 0:
            self.change_balls_cooldown -= 1

    def freeze_cooldown(self):
        self.cooldown = 5

    def freeze_change_cooldown(self):
        self.change_balls_cooldown = 250

    def tick(self):
        self.task_manager.task_tick()
        self.down_cooldowns()

    def add_task(self, task):
        self.task_manager.add_task(task)
