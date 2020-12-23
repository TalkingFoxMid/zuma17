from PyQt5.QtGui import QPixmap


class PausaAnimation:
    def __init__(self):
        self.ended = False
        self.ticks_remain = 20

    def draw(self, qp):
        qp.setOpacity(self.get_opacity())
        qp.drawPixmap(150, 100, 312 * 1.5, 153 * 1.5, QPixmap("resources/pausa_png.png"))
        qp.setOpacity(1)

    def get_opacity(self):
        if self.ticks_remain > 15:
            return (20 - self.ticks_remain) / 10
        if self.ticks_remain > 10:
            return 1
        else:
            return self.ticks_remain / 10

    def tick(self):
        self.ticks_remain -= 1
        if self.ticks_remain < 0:
            self.ended = True
