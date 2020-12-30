from animation_manager.animation_manager import AnimationManager
from game_logic.balls_conveyor import BallsConveyor
from game_logic.frog_operator import FrogOperator
from task_manager.task_manager import TaskManager
from task_manager.task_normalize_space import TaskNormalizeSpace


class GameState:
    """Инкапсулирует всю игровую логику"""

    def __init__(self, game_level, random_color_manager):
        self.angle = 0
        self.random_color_manager = random_color_manager
        self.animation_manager = AnimationManager()
        self.game_level = game_level

        self.balls = []
        self.frog_operator = FrogOperator(self)
        self.task_manager = TaskManager()
        self.time_space_opacity = 0
        self.score = 0
        self.lost = False
        self.game_ended_win = False
        self.balls_conveyor = BallsConveyor(self, game_level)

    def set_animation_manager(self, animation_manager):
        self.animation_manager = animation_manager

    def tick(self):
        if (
                len(self.balls_conveyor.balls_list) == 0
                and self.balls_conveyor.no_balls_remain
        ):
            self.game_ended_win = True
        self.task_manager.task_tick()
        self.balls_conveyor.tick()
        self.tick_flying_balls()
        self.frog_operator.down_cooldowns()
        self.balls_conveyor.place_balls()

    def tick_flying_balls(self):
        for i in self.balls:
            if i.color == "TIME":
                self.time_space_opacity += 0.01

                if self.time_space_opacity > 1:
                    self.time_space_opacity = 1
                self.balls_conveyor.speed = 0
                i.speed = 2
            if i.must_been_deleted:
                if i.color == "TIME":
                    self.task_manager.add_task(
                        TaskNormalizeSpace(self)
                    )
                    self.balls_conveyor.speed = 1
                self.balls.remove(i)
        for i in self.balls:
            i.tick()
            self.balls_conveyor.try_to_inplace_ball(i)
            if i.x > 800 or i.y > 800 or i.x < 0 or i.y < 0:
                i.must_been_deleted = True

    def shot_a_ball(self, angle):
        self.frog_operator.shot_a_ball(angle)

    def swap_balls(self):
        self.frog_operator.swap_balls()

    def change_balls(self):
        self.frog_operator.change_balls()

    def add_task(self, task):
        self.task_manager.add_task(task)
