import math


class AngleProvider:
    """По заданным x и y от начала координат, считает угол
    радиус вектора"""
    def get_angle(self, x, y):
        if x == 0:
            if y > 0:
                return math.pi / 2
            else:
                return -math.pi / 2
        else:
            if x > 0:
                return math.atan(y / x)

            else:
                return math.atan(y / x) + math.pi
