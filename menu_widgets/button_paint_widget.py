from PyQt5.QtCore import QTimer, pyqtSlot, QPoint
from PyQt5.QtGui import QPixmap, QPainter
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout

from mouse_tracker import MouseTracker


class ButtonPaintWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.label = QLabel()
        tracker = MouseTracker(self.label)
        tracker.positionChanged.connect(self.on_position_changed)
        self.buttons = []
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.layout.addWidget(self.label)
        self.background = ""
        self.timer = QTimer()
        self.timer.timeout.connect(self.handle_timer)
        self.timer.start(40)

    def paint_buttons(self):
        for i in self.buttons:
            x, y, w, h = i.get_geometry()
            self.qp.drawPixmap(x, y, w, h, QPixmap(i.get_pixmap()))
            self.qp.drawPixmap(x, y, w, h, QPixmap(i.text_resource))

    def paint_background(self):
        self.qp.drawPixmap(0, 0, 800, 800, QPixmap(self.background))

    def mousePressEvent(self, a0):
        for i in self.buttons:
            if i.is_pressed:
                i.on_click()

    @pyqtSlot(QPoint)
    def on_position_changed(self, pos):
        for i in self.buttons:
            x, y, w, h = i.get_geometry()
            if pos.x() > x and pos.x() < x + w and pos.y() > y and pos.y() < y + h:
                i.is_pressed = True
            else:
                i.is_pressed = False
