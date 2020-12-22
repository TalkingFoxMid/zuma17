class Level2:
    def __init__(self):
        self.remain_balls = 40
        self.frog_position = [390, 400]
        self.score_position = [389, 158]
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
        if p > 0 and p <= 1:
            ball.x, ball.y = 100, p * 700
        if p > 1 and p <= 1.14:
            ball.x, ball.y = 100+700*(p-1), 700
        if p > 1.14 and p <= 2:
            ball.x, ball.y = 200, 700-(p-1.14)*700
        if p > 2 and p <= 2.14:
            ball.x, ball.y = 200+700*(p-2), 100
        if p > 2.14 and p <= 3:
            ball.x, ball.y = 300, 100+700*(p-2.14)
        if p > 3 and p <= 3.28:
            ball.x, ball.y = 300+(p-3)*700, 700
        if p > 3.28 and p <= 4.14:
            ball.x, ball.y = 500, 700-(p-3.28)*700
        if p > 4.14 and p <= 4.28:
            ball.x, ball.y = 500+(p-4.14)*700, 100
        if p > 4.28 and p <= 5.14:
            ball.x, ball.y = 600, 100+(p-4.28)*700
        if p > 5.14 and p <= 5.28:
            ball.x, ball.y = 600+(p-5.14)*700, 700
        if p > 5.28 and p <= 6.28:
            ball.x, ball.y = 700, 700-(p-5.28)*700
        return [ball.x, ball.y]