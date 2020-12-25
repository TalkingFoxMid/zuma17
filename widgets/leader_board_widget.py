from PyQt5.QtGui import QPainter, QPixmap, QFont
from PyQt5.QtWidgets import QWidget, QVBoxLayout

from widgets.button_paint_widget import ButtonPaintWidget
from widgets.menu_button import MenuButton


class LeaderBoardWidget(ButtonPaintWidget):
    """Виджет таблицы лидеров"""
    def __init__(self, main_window,
                 menu_widget,
                 leader_board_manager):
        super().__init__()
        self.menu_widget = menu_widget
        self.buttons = [
            MenuButton(199, 624, "resources/sberzhat.png", self.back),

        ]
        self.leader_board_manager = leader_board_manager
        self.main_window = main_window
        self.background = "resources/parfenon.png"
        self.leader_board_back = "resources/leader_board.png"

    def back(self):
        self.close()
        self.main_window.setCentralWidget(
            type(self.menu_widget)(self.main_window)
        )

    def handle_timer(self):
        self.label.setPixmap(QPixmap(800, 800))
        self.qp = QPainter(self.label.pixmap())
        self.qp.setFont(QFont("arial", 35))

        self.paint_background()
        self.paint_results()
        self.paint_buttons()

        self.qp.end()

    def paint_results(self):
        for i in range(1, 10):
            res = self.leader_board_manager.get_level_result(i)
            if res[0] == "":
                continue
            pos = self.leader_board_manager.get_draw_position(i)
            self.qp.drawText(pos[0],
                             pos[1],
                             f"{res[0]}")
            self.qp.drawText(pos[0],
                             pos[1] + 75,
                             f"{res[1]}")

    def paint_background(self):

        self.qp.drawPixmap(0, 0, 800, 800, QPixmap(self.background))
        self.qp.drawPixmap(0, 0, 800, 800, QPixmap(self.leader_board_back))
