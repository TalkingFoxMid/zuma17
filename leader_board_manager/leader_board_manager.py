import json
import hashlib


class LeaderBoardManager:
    def __init__(self, fs_provider):
        self.results = []
        self.fs_provider = fs_provider
        self.load_from_file()
        while len(self.results) < 9:
            self.results += [["", 0]]

    def load_from_file(self):
        leadboard = self.fs_provider.read_from_file(
            "leaderboard", "r"
        )
        hash = self.fs_provider.read_from_file(
            "lb.hash", "rb"
        )
        if len(leadboard) == 0 or len(hash) == 0:
            return
        results = json.loads(leadboard)
        new_hash = self.get_results_hash(results)
        print(new_hash)
        if (hash != new_hash):
            return
        else:
            self.results = results

    def get_results_hash(self, results):
        return hashlib.md5(
            (json.dumps([results]) + "SALTo_mortale").encode()).digest()

    def save_to_file(self):
        hash = self.get_results_hash(self.results)
        self.fs_provider.write_in_file("leaderboard",
                                       json.dumps(self.results),
                                       "w"
                                       )
        self.fs_provider.write_in_file("lb.hash",
                                       hash,
                                       "wb")

    def get_level_result(self, level):
        if len(self.results) < level:
            return "", 0
        return self.results[level - 1]

    def set_result(self, result):
        if self.results[result[0] - 1][1] < result[1][1]:
            self.results[result[0] - 1] = result[1]
        self.save_to_file()

    def get_draw_position(self, level):
        mapping = [
            [150, 125],
            [350, 125],
            [550, 155],
            [150, 325],
            [340, 335],
            [550, 355],
            [150, 525],
            [340, 525],
            [550, 525]
        ]
        return mapping[level - 1]
