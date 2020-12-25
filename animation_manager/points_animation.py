from PyQt5.QtGui import QPixmap, QFont, QColor


class PointsAnimation:
    def __init__(self, x, y, points, color):
        self.ended = False
        self.x = x
        self.y = y
        self.color = color
        self.points = points
        self.ticks_remain = 20

    def draw(self, qp):

        qp.setPen(QColor(self.color))
        qp.setFont(QFont("arial", (self.points - 20) * 2))
        qp.drawText(self.x, self.y - 2 * self.get_bias(),
                    "+" + str(self.points))

    def get_bias(self):
        return 20 - self.ticks_remain

    def tick(self):
        self.ticks_remain -= 1
        if self.ticks_remain < 0:
            self.ended = True
