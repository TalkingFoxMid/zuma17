from PyQt5 import QtCore, QtGui, QtWidgets

from game_widget import BaseWidget


class MouseTracker(QtCore.QObject):
    positionChanged = QtCore.pyqtSignal(QtCore.QPoint)

    def __init__(self, widget):
        super().__init__(widget)
        self._widget = widget
        self.widget.setMouseTracking(True)
        self.widget.installEventFilter(self)

    @property
    def widget(self):
        return self._widget

    def eventFilter(self, o, e):
        if o is self.widget and e.type() == QtCore.QEvent.MouseMove:
            self.positionChanged.emit(e.pos())
        return super().eventFilter(o, e)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        central_widget = QtWidgets.QWidget()
        self.setCentralWidget(central_widget)
        self.base_widget = BaseWidget()

        self.video_label = QtWidgets.QLabel()
        self.video_label.setStyleSheet("background-color: green; border: 1px solid black")

        tracker = MouseTracker(self.base_widget.label)
        tracker.positionChanged.connect(self.on_positionChanged)

        lay = QtWidgets.QVBoxLayout(central_widget)
        lay.addWidget(self.base_widget)
        lay.addWidget(QtWidgets.QLabel())

        self.resize(640, 480)


    @QtCore.pyqtSlot(QtCore.QPoint)
    def on_positionChanged(self, pos):
        print(pos)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())