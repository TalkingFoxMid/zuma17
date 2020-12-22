from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QWidget


class ButtonPaintWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.buttons_main_menu = []
        self.timer = QTimer()
        self.timer.timeout.connect(self.handle_timer)
        self.timer.start(40)
