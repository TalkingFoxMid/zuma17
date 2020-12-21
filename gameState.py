from balls_conveyor import BallsConveyor
from task_manager import TaskManager


class GameState:
    def __init__(self, game_level):
        self.angle = 0
        self.game_level = game_level
        self.balls_conveyor = BallsConveyor(self, game_level)
        self.balls = []
        self.task_manager = TaskManager()
        self.next_color = 'red'
        self.score = 0

    def get_angle(self):
        return self.angle

    def tick(self):
        self.task_manager.task_tick()

    def add_task(self, task):
        self.task_manager.add_task(task)