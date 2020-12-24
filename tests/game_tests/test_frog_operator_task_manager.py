from game_logic.game_state import GameState
from game_levels.level1_river import Level1
from special_providers.random_color_provider import RandomColorManager
import unittest

class TestFrogOperator(unittest.TestCase):
    def test_frog_operator_task_manager(self):
        game_state = GameState(Level1(),
                               RandomColorManager(17))
        for i in range(3):
            game_state.frog_operator.shot_a_ball(0)
            game_state.tick()
        for i in range(5):
            game_state.tick()

        game_state.frog_operator.swap_balls()
        assert game_state.frog_operator.balls_swap_parameter2 == 1
        game_state.tick()
        assert game_state.frog_operator.balls_swap_parameter2 == 0.8
        for i in range(4):
            game_state.tick()
        assert game_state.frog_operator.first_ball_color == "red"
        assert game_state.frog_operator.second_ball_color == "yellow"
        assert game_state.frog_operator.third_ball_color == "red"
        assert game_state.frog_operator.balls_swap_parameter2 == 0
        game_state.frog_operator.change_balls()
        assert game_state.frog_operator.first_ball_color == "green"
        assert game_state.frog_operator.second_ball_color == "green"
        assert game_state.frog_operator.third_ball_color == "green"
