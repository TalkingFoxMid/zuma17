from PyQt5.QtCore import QTimer, pyqtSignal, QPoint, QEvent, QObject, pyqtSlot
from PyQt5.QtGui import QPixmap, QPainter, QColor, QMouseEvent, QCursor
from PyQt5.QtWidgets import QWidget, QLabel
from PyQt5.QtWidgets import QGridLayout

from canvasLabel import CanvasLabel
from conveyor_ball import ConveyorBall
from flyingBall import FlyingBall
from gameState import GameState
import math
import random

from random_color_manager import RandomColorManager


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
        self.random_color_manager = RandomColorManager()
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
        self.counter = 0




    def handle_timer(self):
        self.game_state.tick()
        self.counter += 1
        self.game_state.balls_conveyor.place_balls()
        if self.x == 0:
            self.angle = math.pi/2
        else:
            self.angle = math.atan(self.y/self.x)

            if self.x < 0:
                self.angle = math.atan(self.y / self.x)+math.pi
        self.draw_game_state()

    def mousePressEvent(self, a0: QMouseEvent) -> None:
        self.game_state.balls.append(FlyingBall(angle=self.angle,
                                     color=self.random_color_manager.get_random_color()))

    def draw_game_state(self):
        self.label.pixmap().fill(QColor(255,255,255))
        self.qp = QPainter(self.label.pixmap())
        self.qp.setPen(QColor(200,0,0))
        self.draw_central_frog()
        self.draw_conveyor_balls()
        self.draw_flying_balls()
        self.qp.end()
        self.update()
    def draw_flying_balls(self):
        for i in self.game_state.balls:
            if i.must_been_deleted:
                self.game_state.balls.remove(i)
        for i in self.game_state.balls:
            i.tick()
            if self.game_state.balls_conveyor.try_to_inplace_ball(
                i
            ):
                continue
            if i.x > 800 or i.y > 800 or i.x < 0 or i.y < 0:
                self.game_state.balls.remove(i)
                continue
            ball_color = self.random_color_manager.get_qt_color_from_string(i.color)
            self.qp.setPen(ball_color)
            self.qp.setBrush(ball_color)

            self.qp.drawEllipse(i.x-10, i.y-10, 30, 30)

    def draw_conveyor_balls(self):
        self.game_state.balls_conveyor.tick()
        for i in self.game_state.balls_conveyor.get_balls_list():
            x, y = self.game_state.balls_conveyor.get_ball_position(i)
            ball_color = self.random_color_manager.get_qt_color_from_string(i.color)
            self.qp.setPen(ball_color)
            self.qp.setBrush(ball_color)
            self.qp.drawEllipse(x, y, 42, 42)

    def draw_central_frog(self):
        angle = self.game_state.get_angle()
        self.qp.drawEllipse(400,400,30,30)
        self.qp.drawLine(415,415,415+100*math.cos(self.angle),
                         415+100*math.sin(self.angle))

    @pyqtSlot(QPoint)
    def on_positionChanged(self, pos):
        self.x = pos.x()-415
        self.y = pos.y()-415





