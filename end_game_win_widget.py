from PyQt5.QtCore import pyqtSlot, QPoint


class EndGameWinWidget:
    def __init__(self):
        super().__init__()
        self.buttons = []

    @pyqtSlot(QPoint)
    def on_positionChanged(self, pos):
        for i in self.buttons:
            x, y, w, h = i.get_geometry()
            if pos.x() > x and pos.x() < x + w and pos.y() > y and pos.y() < y + h:
                i.is_pressed = True
            else:
                i.is_pressed = False