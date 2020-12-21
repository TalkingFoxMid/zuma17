import math
class MenuBall:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.angle = 3*math.pi/4
        self.speed = 4
    def tick(self):
        self.x += math.cos(self.angle)*self.speed
        self.y += math.sin(self.angle)*self.speed