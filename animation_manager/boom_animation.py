from PyQt5.QtGui import QPixmap, QFont, QColor


class BoomAnimation:
    def __init__(self, x, y):
        self.ended = False
        self.x = x
        self.y = y
        self.ticks_remain = 24

    def draw(self, qp):
        qp.drawPixmap(self.x-100, self.y-200, 200, 200, self.get_pixmap())

    def get_pixmap(self):
        print(self.ticks_remain)
        return QPixmap(f"resources/boom_gif/YQDj-{24 - self.ticks_remain}.png")

    def tick(self):
        self.ticks_remain -= 1
        if self.ticks_remain < 0:
            self.ended = True
