from PyQt5.QtGui import QPixmap


class TipAnimation:
    def __init__(self):
        self.ended = False
        self.ticks_remain = 50
    def draw(self, qp):
        qp.setOpacity(self.get_opacity())
        qp.drawPixmap(400, 600, 300, 100, QPixmap("resources/tip.png"))
        qp.setOpacity(1)
    def get_opacity(self):
        if self.ticks_remain > 20:
            return 1
        else:
            return self.ticks_remain/10
    def tick(self):
        self.ticks_remain -= 1
        if self.ticks_remain < 0:
            self.ended = True