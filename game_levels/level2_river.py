class Level2:
    def __init__(self):
        self.remain_balls = 80
        self.frog_position = [390, 400]
        self.score_position = [389, 158]
        self.number = 2
        self.map_resource = "resources/map2.png"

    def take_ball(self):
        if self.remain_balls > 0:
            self.remain_balls -= 1
            return True
        else:
            return False

    def get_max_parameter(self):
        return 6.20

    def get_ball_position(self, ball):
        p = ball.parameter
        if 0 <= p <= 1:
            ball.x, ball.y = 100, p * 700
        if 1 < p <= 1.14:
            ball.x, ball.y = 100 + 700 * (p - 1), 700
        if 1.14 < p <= 2:
            ball.x, ball.y = 200, 700 - (p - 1.14) * 700
        if 2 < p <= 2.14:
            ball.x, ball.y = 200 + 700 * (p - 2), 100
        if 2.14 < p <= 3:
            ball.x, ball.y = 300, 100 + 700 * (p - 2.14)
        if 3 < p <= 3.28:
            ball.x, ball.y = 300 + (p - 3) * 700, 700
        if 3.28 < p <= 4.14:
            ball.x, ball.y = 500, 700 - (p - 3.28) * 700
        if 4.14 < p <= 4.28:
            ball.x, ball.y = 500 + (p - 4.14) * 700, 100
        if 4.28 < p <= 5.14:
            ball.x, ball.y = 600, 100 + (p - 4.28) * 700
        if 5.14 < p <= 5.28:
            ball.x, ball.y = 600 + (p - 5.14) * 700, 700
        if 5.28 < p <= 6.28:
            ball.x, ball.y = 700, 700 - (p - 5.28) * 700
        return [ball.x, ball.y]
