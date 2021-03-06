class Level1:
    def __init__(self):
        self.remain_balls = 40
        self.frog_position = [400, 400]
        self.score_position = [500, 265]
        self.number = 1
        self.map_resource = "resources/map.png"

    def take_ball(self):
        if self.remain_balls > 0:
            self.remain_balls -= 1
            return True
        else:
            return False

    def get_max_parameter(self):
        return 5.69

    def get_ball_position(self, ball):
        p = ball.parameter
        if 0 <= p <= 1:
            ball.x, ball.y = ball.parameter * 700, 100
        elif 1 < p <= 1.85:
            ball.x, ball.y = 700, 100 + (p - 1) * 700
        elif 1.85 < p <= 2.7:
            ball.x, ball.y = 700 - (p - 1.85) * 700, 700
        elif 2.7 < p <= 3.41:
            ball.x, ball.y = 100, 700 - (p - 2.7) * 700
        elif 3.41 < p <= 4.12:
            ball.x, ball.y = 100 + (p - 3.41) * 700, 200
        elif 4.12 < p <= 4.69:
            ball.x, ball.y = 600, 200 + (p - 4.12) * 700
        elif 4.69 < p <= 5.26:
            ball.x, ball.y = 600 - (p - 4.69) * 700, 600
        elif 5.26 < p <= 5.69:
            ball.x, ball.y = 200, 600 - (p - 5.26) * 700

        return [ball.x, ball.y]
