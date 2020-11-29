from PyQt5.QtGui import QMouseEvent, QDragMoveEvent, QMoveEvent
from PyQt5.QtWidgets import *
import sys
from baseWidget import BaseWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setCentralWidget(BaseWidget())
        self.setGeometry(0, 0, 800, 800)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    app.exec_()