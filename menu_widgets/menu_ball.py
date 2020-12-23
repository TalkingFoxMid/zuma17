import math


class MenuBall:
    def __init__(self, x, y, color, speed_x, speed_y):
        self.x = x
        self.y = y
        self.color = color
        self.angle = 3 * math.pi / 4
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.friction = 0.0
        self.slowing_down = True

    def tick(self):
        self.x += self.speed_x
        self.y += self.speed_y
        if self.speed_x > self.friction:
            self.speed_x -= self.friction
        if self.speed_x < -self.friction:
            self.speed_x += self.friction
        if self.speed_y > self.friction:
            self.speed_y -= self.friction
        if self.speed_y < -self.friction:
            self.speed_y += self.friction
