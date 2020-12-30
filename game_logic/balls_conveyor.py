import math


from special_providers.color_distribution_provider import \
    ColorDistributionProvider
from game_logic.conveyor_ball import ConveyorBall
from task_manager.task_delete_conveyor_balls import TaskDeleteConveyorBalls


class BallsConveyor:
    """Реализует логику поведения шариков на конвеере"""

    def __init__(self, game_state, maze_level):
        self.balls_list = []
        self.color_distribution_provider = ColorDistributionProvider()
        self.game_state = game_state
        self.speed = 1
        self.last_ball_parameter = 0
        self.random_color_manager = self.game_state.random_color_manager
        self.last_ball = None
        self.no_balls_remain = False

        self.maze_strategy = maze_level

    def get_color_distribution(self):
        return self.color_distribution_provider.get_color_distribution(
            self.balls_list)

    def tick(self):
        for i in self.balls_list:
            i.x, i.y = self.get_ball_position(i)
            if i.parameter > self.maze_strategy.get_max_parameter():
                self.balls_list.remove(i)

                self.game_state.lost = True
                return
            if i.must_been_deleted:
                self.game_state.score += 10

                self.balls_list.remove(i)
        for i in range(len(self.balls_list) - 1, -1, -1):
            if not self.can_ball_go(i):
                continue

            if i == len(self.balls_list) - 1:
                self.balls_list[i].parameter += 0.005 * self.speed
                continue
            distance = (self.balls_list[i].parameter -
                        self.balls_list[i + 1].parameter)
            if distance < 0.08:
                self.balls_list[i].parameter += (
                    ((0.08 - distance) * 0.3)
                )
                if self.balls_list[i].hot and self.balls_list[i + 1].hot:
                    b1 = self.balls_list[i]
                    b2 = self.balls_list[i + 1]
                    self.release_balls(i, True)
                    b1.hot = False
                    b2.hot = False
            else:
                self.balls_list[i].parameter -= 0.005 * self.speed

    def can_ball_go(self, ball_index):
        if self.balls_list[ball_index].unriverable:
            return False
        if ball_index == 0:
            return True
        return self.balls_list[ball_index - 1]

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
        ball.x, ball.y = self.get_ball_position(ball)
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
            else:
                self.no_balls_remain = True

    def release_balls(self, index, hotted=False):
        color = self.balls_list[index].color
        right_edge = index
        left_edge = index
        for i in range(index + 1, len(self.balls_list)):
            if self.balls_list[i].color == color:
                right_edge += 1
                continue
            break
        for i in range(index - 1, -1, -1):
            if self.balls_list[i].color == color:
                left_edge -= 1
                continue
            break

        if right_edge - left_edge + 1 >= 3:
            if hotted:
                print("DELETED_MAXIMUX")
            mid = self.balls_list[int((right_edge + left_edge) / 2)]
            if self.game_state.animation_manager is not None:
                self.game_state.animation_manager.add_points_animation(
                    mid.x,
                    mid.y,
                    10 * (right_edge - left_edge + 1),
                    mid.color
                )
            for i in self.balls_list[left_edge: right_edge + 1]:
                i.unriverable = True

            self.game_state.add_task(
                TaskDeleteConveyorBalls(
                    self.balls_list[left_edge: right_edge + 1],
                    self
                )
            )

    def do_boom(self, x, y):
        boom_list = []
        for i in self.balls_list:
            dx = x - i.x
            dy = y - i.y
            if abs(dx) > 100:
                continue
            if abs(dy) > 100:
                continue
            if math.sqrt(dx * dx + dy * dy) > 200:
                continue
            boom_list.append(i)
        if self.game_state.animation_manager is not None:
            self.game_state.animation_manager.add_boom_animation(
                x, y
            )
        self.game_state.add_task(
            TaskDeleteConveyorBalls(
                boom_list,
                self
            )
        )

    def try_to_inplace_ball(self, flying_ball):
        for i in self.balls_list:
            if i.unriverable:
                continue
            dx = flying_ball.x - i.x
            dy = flying_ball.y - i.y
            if abs(dx) > 42:
                continue
            if abs(dy) > 42:
                continue
            if math.sqrt(dx * dx + dy * dy) > 42:
                continue
            if flying_ball.color == "TIME":
                flying_ball.must_been_deleted = True

                return
            if flying_ball.color == "BOOM":
                flying_ball.must_been_deleted = True
                self.do_boom(flying_ball.x, flying_ball.y)
                return
            index = self.balls_list.index(i)
            new_ball = ConveyorBall(
                flying_ball.color,
                i.parameter + 0.07
            )
            new_ball.x, new_ball.y = self.get_ball_position(new_ball)
            self.balls_list.insert(index, new_ball)
            if index != 0:
                self.balls_list[index - 1].parameter += 0.07
            self.release_balls(index)

            flying_ball.must_been_deleted = True
            return True
        return False
