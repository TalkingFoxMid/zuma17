from PyQt5.QtGui import QColor

from conveyor_ball import ConveyorBall
from conveyor_strategy_maze import ConveyorStategyMaze
from random_color_manager import RandomColorManager
from task_free_place_conveyor import TaskFreePlaceConveyor


class BallsConveyor:
    def __init__(self, game_state):
        self.balls_list = []
        self.game_state = game_state
        self.last_ball_parameter = 0
        self.random_color_manager = RandomColorManager()
        self.last_ball = None

        self.maze_strategy = ConveyorStategyMaze()
    def tick(self):
        for i in self.balls_list:
            if i.parameter > self.maze_strategy.get_max_parameter():
                self.balls_list.remove(i)
        for i in self.balls_list:
            i.parameter += 0.003*5


    def get_ball_position(self, ball):
        return self.maze_strategy.get_ball_position(ball)

    def get_balls_list(self):
        return self.balls_list
    def spawn_ball(self, ball):
        if self.last_ball is None:
            self.last_ball = ball
        self.balls_list.append(ball)
    def spawn_random_ball(self):
        self.spawn_ball(ConveyorBall(
            self.random_color_manager.get_random_color(),
            0
        ))
    def place_balls(self):
        if len(self.balls_list) == 0:
            self.spawn_random_ball()
        if self.balls_list[-1].parameter > 0.07:
            self.spawn_random_ball()
    def try_to_inplace_ball(self, flying_ball):
        for i in self.balls_list:
            if abs(flying_ball.x - i.x) > 15:
                continue
            if abs(flying_ball.y - i.y) > 15:
                continue
            index = self.balls_list.index(i)
            self.game_state.add_task(
                TaskFreePlaceConveyor(self.balls_list[0: index])
            )
            self.balls_list.insert(index, ConveyorBall(
                flying_ball.color,
                i.parameter+0.04
            ))
            flying_ball.must_been_deleted = True
            return True
        return False
