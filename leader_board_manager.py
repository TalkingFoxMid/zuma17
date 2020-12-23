import json
class LeaderBoardManager:
    def __init__(self):
        self.results = []
        self.load_from_file()
    def load_from_file(self):
        with open("leaderboard", "r") as f:
            txt = f.read()

            if len(txt) == 0:
                return
            self.results = json.loads(txt)
    def save_to_file(self):
        with open("leaderboard", "w") as f:
            f.write(json.dumps(self.results))
    def get_level_result(self, level):
        if len(self.results) < level:
            return "", 0
        return self.results[level - 1]
    def set_result(self, result):
        if self.results[result[0]] < result[1]:
            self.results[result[0]] = result[1]
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
        return mapping[level-1]
