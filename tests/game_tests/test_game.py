from game_levels.level1_river import Level1
from game_logic.game_state import GameState
from special_providers.random_color_provider import RandomColorManager
import math


def test_game_state_mass_level1():
    gs = GameState(Level1(),
                   RandomColorManager(17))
    for i in range(100):
        gs.tick()
        gs.shot_a_ball(math.pi)
    assert [i.x for i in gs.balls_conveyor.balls_list] == [319.1727070332252,
                                                           270.6653360097429,
                                                           222.03318192890103,
                                                           173.29641567834392,
                                                           124.58262563354253,
                                                           76.10235738, 28.0]
    for i in range(100):
        gs.tick()
        gs.shot_a_ball(math.pi)
    assert [i.x for i in gs.balls_conveyor.balls_list][0:3] == [642.1161871315678, 593.65417355924, 545.1793958916618]
    assert [i.x for i in gs.balls] == [7.0, 92.0, 177.0, 262.0, 347.0]
    for i in range(100):
        gs.tick()
        gs.frog_operator.swap_balls()
        gs.shot_a_ball(math.pi)
    assert [i.y for i in gs.balls_conveyor.balls_list][0:3] == [365.17841697693757,
                                                                316.71719336128933,
                                                                268.2547669983126]
    for i in range(892):
        gs.tick()
        gs.frog_operator.swap_balls()
        gs.shot_a_ball(math.pi)
    assert gs.lost is False
    gs.tick()
    gs.frog_operator.swap_balls()
    gs.shot_a_ball(math.pi)
    assert gs.lost is True


if __name__ == '__main__':
    test_game_state_mass_level1()
