from PyQt5.QtCore import QTimer, pyqtSignal, QPoint, QEvent, QObject, pyqtSlot
from PyQt5.QtGui import QPixmap, QPainter, QColor, QMouseEvent, QCursor
from PyQt5.QtWidgets import QWidget, QLabel
from PyQt5.QtWidgets import QGridLayout

from canvasLabel import CanvasLabel
from gameState import GameState
import math

class MouseTracker(QObject):
    positionChanged = pyqtSignal(QPoint)

    def __init__(self, widget):
        super().__init__(widget)
        self._widget = widget
        self.widget.setMouseTracking(True)
        self.widget.installEventFilter(self)

    @property
    def widget(self):
        return self._widget

    def eventFilter(self, o, e):
        if o is self.widget and e.type() == QEvent.MouseMove:
            self.positionChanged.emit(e.pos())
        return super().eventFilter(o, e)
class BaseWidget(QWidget):
    positionChanged = pyqtSignal(QPoint)
    def __init__(self):
        super().__init__()
        self.x = 1
        self.y = 1

        self.game_state = GameState()
        self.grid = QGridLayout()
        self.canvas = QPixmap(800, 800)
        self.label = CanvasLabel()
        self.label.setPixmap(self.canvas)
        tracker = MouseTracker(self.label)
        tracker.positionChanged.connect(self.on_positionChanged)
        self.grid.addWidget(self.label)
        self.setLayout(self.grid)
        self.timer = QTimer()
        self.timer.timeout.connect(self.handle_timer)
        self.timer.start(40)



    def handle_timer(self):
        if self.x == 0:
            self.angle = math.pi/2
        else:
            self.angle = math.atan(self.y/self.x)

            if self.x < 0:
                self.angle = math.atan(self.y / self.x)+math.pi
        self.draw_game_state()

    def draw_game_state(self):
        self.qp = QPainter(self.label.pixmap())
        self.qp.setPen(QColor(200,0,0))
        self.draw_central_frog()
        self.qp.end()
        self.update()

    def draw_central_frog(self):
        angle = self.game_state.get_angle()
        self.qp.drawEllipse(400,400,30,30)
        self.qp.drawLine(415,415,415+100*math.cos(self.angle),
                         415+100*math.sin(self.angle))

    @pyqtSlot(QPoint)
    def on_positionChanged(self, pos):
        print(pos)





