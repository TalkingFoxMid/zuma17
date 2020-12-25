import math


class FlyingBall:
    """Инкапсулирует состояние шарика в полёте"""
    def __init__(self, x=415, y=415, angle=0, color="red"):
        super().__init__()
        self.x = x
        self.y = y
        self.angle = angle
        self.speed = 17
        self.must_been_deleted = False
        self.color = color

    def tick(self):
        self.x += math.cos(self.angle) * self.speed
        self.y += math.sin(self.angle) * self.speed
