from leader_board_manager.leader_board_manager import LeaderBoardManager
from special_providers.test_fs_provider import TestFsProvider


def test_leader_board():
    lb = LeaderBoardManager(TestFsProvider())
    lb.set_result([1, ["lol", 280]])
    lb.set_result([1, ["dim", 135]])
    lb.set_result([5, ["v", 55]])
    assert lb.get_level_result(1)[1] == 280
    assert lb.get_level_result(5)[1] == 55
