import math

from game_logic.game_state import GameState
from game_levels.level1_river import Level1
from game_levels.level2_river import Level2
from special_providers.random_color_provider import RandomColorManager
import unittest


class TestFrogOperatorTaskManager(unittest.TestCase):
    def test_frog_operator_shot_balls_placing(self):
        game_state = GameState(Level1(),
                               RandomColorManager(17))
        for i in range(121):
            game_state.shot_a_ball(1)
            game_state.tick()
        assert [i.x for i in game_state.balls_conveyor.balls_list][:5] == \
               [386.82811800632334, 338.2810698121899,
                289.7447066270861, 241.2829164862018,
                192.96513676485594]

    def test_frog_operator_balls_swaping(self):
        game_state = GameState(Level1(),
                               RandomColorManager(21))
        for i in range(121):
            game_state.shot_a_ball(1)
            game_state.swap_balls()
            game_state.tick()
        assert ([game_state.frog_operator.first_ball_color,
                 game_state.frog_operator.second_ball_color,
                 game_state.frog_operator.third_ball_color]
                == ['red', 'green', 'red'])

    def test_frog_operator_change_balls(self):
        game_state = GameState(Level2(),
                               RandomColorManager(21))
        for i in range(121):
            game_state.shot_a_ball(1)
            game_state.change_balls()
            game_state.tick()
        assert ([game_state.frog_operator.first_ball_color,
                 game_state.frog_operator.second_ball_color,
                 game_state.frog_operator.third_ball_color]
                == ['blue', 'yellow', 'yellow'])

    def test_frog_shot_combo(self):
        game_state = GameState(Level2(),
                               RandomColorManager(1))
        for i in range(300):
            game_state.tick()
            game_state.frog_operator.shot_a_ball(math.pi)
        assert ([i.color for i in game_state.balls_conveyor.balls_list[:10]]
                == ['red', 'green', 'blue', 'red', 'yellow', 'yellow',
                    'green', 'yellow', 'blue', 'red'])
