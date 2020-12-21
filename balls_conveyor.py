from PyQt5.QtGui import QColor
import sys
from conveyor_ball import ConveyorBall
from random_color_manager import RandomColorManager
from task_delete_conveyor_balls import TaskDeleteConveyorBalls
from task_free_place_conveyor import TaskFreePlaceConveyor


class BallsConveyor:
    def __init__(self, game_state, maze_level):
        self.balls_list = []
        self.game_state = game_state
        self.last_ball_parameter = 0
        self.random_color_manager = RandomColorManager()
        self.last_ball = None

        self.maze_strategy = maze_level
    def tick(self):
        for i in self.balls_list:
            if i.parameter > self.maze_strategy.get_max_parameter():
                self.balls_list.remove(i)
                sys.exit(1)
                continue
            if i.must_been_deleted:
                self.game_state.score += 10
                self.balls_list.remove(i)
        for i in range(len(self.balls_list)-1,-1,-1):
            if not self.can_ball_go(i):
                continue

            if i == len(self.balls_list)-1:
                self.balls_list[i].parameter += 0.005
                continue
            distance = self.balls_list[i].parameter - self.balls_list[i+1].parameter
            if distance < 0.08:
                self.balls_list[i].parameter += ((0.08-distance)*0.3)




    def can_ball_go(self, ball_index):
        if self.balls_list[ball_index].unriverable:
            return False
        if ball_index == 0:
            return True
        return self.balls_list[ball_index-1]
    def get_ball_position(self, ball):
        if not ball.unriverable:
            return self.maze_strategy.get_ball_position(ball)
        else:
            return [ball.x, ball.y]

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
        if len(self.balls_list) == 0 or self.balls_list[-1].parameter > 0.07:
            if self.maze_strategy.take_ball():
                self.spawn_random_ball()
    def release_balls(self, index):
        color = self.balls_list[index].color
        right_edge = index
        left_edge = index
        for i in range(index+1, len(self.balls_list)):
            if self.balls_list[i].color == color:
                right_edge += 1
                continue
            break
        for i in range(index-1, -1, -1):
            if self.balls_list[i].color == color:
                left_edge -= 1
                continue
            break

        if right_edge - left_edge + 1 >= 3:
            for i in self.balls_list[left_edge: right_edge+1]:
                i.x, i.y = self.get_ball_position(i)
                i.unriverable = True
            self.game_state.add_task(
                TaskDeleteConveyorBalls(
                    self.balls_list[left_edge: right_edge+1]
                )
            )


        print(left_edge,index, right_edge)

    def try_to_inplace_ball(self, flying_ball):
        for i in self.balls_list:
            if i.unriverable:
                continue
            if abs(flying_ball.x - i.x) > 30:
                continue
            if abs(flying_ball.y - i.y) > 30:
                continue
            index = self.balls_list.index(i)

            self.balls_list.insert(index, ConveyorBall(
                flying_ball.color,
                i.parameter+0.07
            ))
            if index != 0:
                self.balls_list[index - 1].parameter += 0.07
            self.release_balls(index)

            flying_ball.must_been_deleted = True
            return True
        return False
