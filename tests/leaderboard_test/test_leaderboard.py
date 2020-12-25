import unittest

from leader_board_manager.leader_board_manager import LeaderBoardManager
from special_providers.test_fs_provider import TestFsProvider


class TestLeaderBoard(unittest.TestCase):
    def test_leader_board_set_get_result(self):
        lb = LeaderBoardManager(TestFsProvider())
        lb.set_result([1, ["lol", 280]])
        assert lb.get_level_result(1)[1] == 280

    def test_leader_board_not_set_lower_result(self):
        lb = LeaderBoardManager(TestFsProvider())
        lb.set_result([1, ["lol", 280]])
        lb.set_result([1, ["tupple", 270]])
        assert lb.get_level_result(1)[1] == 280

    def test_leader_board_not_set_same_result(self):
        lb = LeaderBoardManager(TestFsProvider())
        lb.set_result([1, ["lol", 280]])
        lb.set_result([1, ["tupple", 280]])
        assert lb.get_level_result(1)[0] == "lol"

    def test_leader_board_set_better_result(self):
        lb = LeaderBoardManager(TestFsProvider())
        lb.set_result([1, ["lol", 280]])
        lb.set_result([1, ["tupple", 290]])
        assert lb.get_level_result(1)[0] == "tupple"
