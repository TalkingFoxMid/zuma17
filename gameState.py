from balls_conveyor import BallsConveyor
from task_manager import TaskManager


class GameState:
    def __init__(self):
        self.angle = 0
        self.balls_conveyor = BallsConveyor(self)
        self.balls = []
        self.task_manager = TaskManager()

    def get_angle(self):
        return self.angle
    def tick(self):
        self.task_manager.task_tick()
    def add_task(self, task):
        self.task_manager.add_task(task)