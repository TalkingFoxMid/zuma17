from PyQt5.QtWidgets import QWidget

from menu_widgets.button_paint_widget import ButtonPaintWidget


class LeaderBoardWidget(ButtonPaintWidget):
    def __init__(self):
        super().__init__()
    def handle_timer(self):
        print("sdaf")
