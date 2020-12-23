from PyQt5.QtCore import pyqtSlot, QPoint, QTimer
from PyQt5.QtGui import QPixmap, QPainter, QFont, QColor
from PyQt5.QtWidgets import QLabel, QWidget, QVBoxLayout

from end_game_win_widget import EndGameWinWidget
from menu_widgets.button_paint_widget import ButtonPaintWidget
from menu_widgets.menu_button import MenuButton
from mouse_tracker import MouseTracker


class EndGameLoseWidget(ButtonPaintWidget):
    def __init__(self, main_window, menu_widget):
        super().__init__()
        self.main_window = main_window
        self.menu_widget = menu_widget
        self.background = "resources/game_end.png"
        self.wasted_position_y = -100
        self.buttons = [
            MenuButton(199, 624, "resources/exit_text.png", self.back)

        ]

    def handle_timer(self):
        self.wasted_position_y += 3
        self.label.setPixmap(QPixmap(800, 800))

        self.qp = QPainter(self.label.pixmap())
        self.paint_background()
        self.qp.drawPixmap(200, self.wasted_position_y - 100,
                           400, 200,
                           QPixmap("resources/frog.png"))
        self.qp.drawPixmap(200, self.wasted_position_y,
                           400, 100,
                           QPixmap("resources/wasted.png"))
        self.paint_buttons()

        self.qp.end()

    def back(self):
        self.close()
        self.main_window.setCentralWidget(
            type(self.menu_widget)(self.main_window)
        )
