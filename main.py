from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtWidgets import *
import sys
from menu_widgets.menu_widget import MenuWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.menu_widget = MenuWidget(self)
        self.setCentralWidget(self.menu_widget)
        self.setGeometry(0, 0, 800, 800)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    app.exec_()