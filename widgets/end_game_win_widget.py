from PyQt5.QtCore import pyqtSlot, QPoint, QTimer
from PyQt5.QtGui import QPixmap, QPainter, QFont, QColor
from PyQt5.QtWidgets import QLabel, QWidget, QVBoxLayout

from widgets.menu_button import MenuButton
from widgets.mouse_tracker import MouseTracker


class EndGameWinWidget(QWidget):
    """Виджет, в случае выигрыша"""

    def __init__(self, main_window, menu_widget, score, lvl):
        super().__init__()
        self.buttons = [
            MenuButton(199, 624, "resources/menu_text.png", self.back)
        ]
        self.lvl = lvl
        self.name = "Convert"
        self.menu_widget = menu_widget
        self.main_window = main_window
        self.score = score
        self.timer = QTimer()
        self.timer.timeout.connect(self.handle_timer)
        self.timer.start(40)
        self.label = QLabel()
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.layout.addWidget(self.label)
        tracker = MouseTracker(self.label)
        tracker.positionChanged.connect(self.on_position_changed)

    def handle_timer(self):

        self.label.setPixmap(QPixmap(800, 800))
        self.qp = QPainter(self.label.pixmap())
        self.qp.setFont(QFont("arial", 55))
        self.qp.setPen(QColor("blue"))
        self.qp.drawPixmap(0, 0, 800, 800,
                           QPixmap("resources/game_end.png"))
        self.qp.drawPixmap(150, 100, 500, 150,
                           QPixmap("resources/pobeda_text.png"))
        self.qp.drawPixmap(100, 300, 500, 150,
                           QPixmap("resources/you_get_score.png"))
        self.qp.drawPixmap(600, 300, 200, 150,
                           QPixmap("resources/table.png"))
        self.qp.drawText(650, 400, str(self.score))
        self.qp.drawPixmap(250, 500, 450, 150,
                           QPixmap("resources/table.png"))

        self.qp.drawText(250, 600, str(self.name))
        self.qp.drawPixmap(0, 500, 200, 150,
                           QPixmap("resources/paste_nick.png"))

        self.paint_buttons()
        self.qp.end()
        self.update()

    def paint_buttons(self):
        for i in self.buttons:
            x, y, w, h = i.get_geometry()
            self.qp.drawPixmap(x, y, w, h, QPixmap(i.get_pixmap()))
            self.qp.drawPixmap(x, y, w, h, QPixmap(i.text_resource))

    def back(self):
        print(self.main_window, self.menu_widget)
        self.close()
        self.menu_widget.set_result([self.lvl,
                                     [self.name, self.score]

                                     ])
        self.main_window.setCentralWidget(
            type(self.menu_widget)(self.main_window)
        )

    def mousePressEvent(self, a0):
        for i in self.buttons:
            if i.is_pressed:
                i.on_click()

    def add_name_symbol(self, symbol):
        if len(self.name) > 10:
            return
        self.name += symbol

    def remove_name_symbol(self):
        if len(self.name) > 0:
            self.name = self.name[0: -1]

    @pyqtSlot(QPoint)
    def on_position_changed(self, pos):
        for i in self.buttons:
            x, y, w, h = i.get_geometry()
            if (pos.x() > x and
                    pos.x() < x + w
                    and pos.y() > y
                    and pos.y() < y + h):
                i.is_pressed = True
            else:
                i.is_pressed = False
