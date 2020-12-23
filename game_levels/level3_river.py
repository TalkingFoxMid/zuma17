class Level3:
    def __init__(self):
        self.remain_balls = 17
        self.frog_position = [390, 400]
        self.score_position = [389, 158]
        self.number = 3
        self.map_resource = "resources/map3.png"

    def take_ball(self):
        if self.remain_balls > 0:
            self.remain_balls -= 1
            return True
        else:
            return False

    def get_max_parameter(self):
        return 2

    def get_ball_position(self, ball):
        p = ball.parameter
        if 0 <= p <= 1:
            ball.x, ball.y = 800 - p * 750, 100
        if 1 < p <= 2:
            ball.x, ball.y = 750 - (p - 1) * 750, 700
        return [ball.x, ball.y]
