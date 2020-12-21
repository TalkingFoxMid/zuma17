from PyQt5.QtCore import QTimer, pyqtSignal, QPoint, QEvent, QObject, pyqtSlot
from PyQt5.QtGui import QPixmap, QPainter, QColor, QMouseEvent, QCursor, QFont, QPen
from PyQt5.QtWidgets import QWidget, QLabel
from PyQt5.QtWidgets import QGridLayout

from canvasLabel import CanvasLabel
from conveyor_ball import ConveyorBall
from flyingBall import FlyingBall
from gameState import GameState
import math
import random

from mouse_tracker import MouseTracker
from random_color_manager import RandomColorManager
from task_reset_parameter import TaskResetParameter


class GameWidget(QWidget):
    positionChanged = pyqtSignal(QPoint)
    def __init__(self, game_level):
        super().__init__()
        self.game_level = game_level
        self.balls_float_animation = 0
        self.x = 1
        self.y = 1
        self.random_color_manager = RandomColorManager()
        self.game_state = GameState(game_level)
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




    def addBallsFloatParameter(self):
        self.balls_float_animation += 0.2
    def handle_timer(self):
        self.addBallsFloatParameter()
        self.game_state.tick()
        self.counter += 1
        self.game_state.balls_conveyor.place_balls()
        if self.x == 0:
            if self.y > 0:
                self.angle = math.pi/2
            else:
                self.angle = -math.pi/2
        else:
            self.angle = math.atan(self.y/self.x)

            if self.x < 0:
                self.angle = math.atan(self.y / self.x)+math.pi
        self.draw_game_state()
    def shotABall(self):

        self.game_state.balls_swap_parameter = 1
        self.game_state.add_task(TaskResetParameter(self.game_state, True, False))
        clr = self.game_state.first_ball_color
        self.game_state.first_ball_color = self.game_state.second_ball_color
        self.game_state.second_ball_color = self.game_state.third_ball_color
        self.game_state.third_ball_color = self.random_color_manager.get_random_color()

        self.game_state.balls.append(FlyingBall(angle=self.angle,
                                                color=clr))
        self.game_state.next_color = self.random_color_manager.get_random_color()
    def swapBalls(self):

        tmp = self.game_state.first_ball_color
        self.game_state.first_ball_color = self.game_state.second_ball_color
        self.game_state.second_ball_color = self.game_state.third_ball_color
        self.game_state.third_ball_color = tmp
        self.game_state.balls_swap_parameter = 1
        self.game_state.balls_swap_parameter2 = 1

        self.game_state.add_task(TaskResetParameter(self.game_state, True, True))

    def mousePressEvent(self, a0: QMouseEvent) -> None:
        if a0.button() == 1:
            self.shotABall()
        elif a0.button() == 2:
            self.swapBalls()


    def draw_game_state(self):
        self.label.setPixmap(QPixmap(self.game_level.map_resource))
        self.qp = QPainter(self.label.pixmap())
        self.qp.setFont(QFont("arial", 22))

        self.qp.setPen(QColor(200,0,0))
        self.draw_central_frog()
        self.draw_conveyor_balls()
        self.draw_flying_balls()
        self.draw_score()
        self.qp.end()
        self.update()
    def draw_score(self):
        self.qp.setPen(QColor(0,0,0))
        x, y = self.game_level.score_position
        self.qp.drawText(x, y, str(self.game_state.score))
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
            self.qp.setPen(QPen(QColor("black"), 3))
            self.qp.setBrush(ball_color)

            self.qp.drawEllipse(i.x-10, i.y-10, 30, 30)

    def draw_conveyor_balls(self):
        self.game_state.balls_conveyor.tick()
        for i in self.game_state.balls_conveyor.get_balls_list():
            x, y = self.game_state.balls_conveyor.get_ball_position(i)
            ball_color = self.random_color_manager.get_qt_color_from_string(i.color)

            self.qp.setBrush(ball_color)

            self.qp.drawEllipse(x-21, y-21, i.diameter, i.diameter)

    def draw_central_frog(self):

        angle = self.game_state.get_angle()

        self.qp.setPen(QPen(QColor("black"), 3))
        x, y = self.game_level.frog_position
        self.qp.drawPixmap(x-35, y-50, QPixmap("resources/frog.png"))
        p = self.game_state.balls_swap_parameter
        p2 = self.game_state.balls_swap_parameter2
        self.qp.setBrush(QColor(self.game_state.first_ball_color))
        self.qp.drawEllipse(x+40*p,y-60*p,30-15*p,30-15*p)

        self.qp.setBrush(QColor(self.game_state.second_ball_color))
        self.qp.drawEllipse(x+40-80*p, y-60+10*math.sin(self.balls_float_animation), 15, 15)

        self.qp.setBrush(QColor(self.game_state.third_ball_color))
        self.qp.drawEllipse(x-40+40*p2, y-60+60*p2+10*math.sin(self.balls_float_animation), 15-15*p+30*p2, 15-15*p+30*p2)

        self.qp.drawLine(x+15,y+15,x+15+100*math.cos(self.angle),
                         y+15+100*math.sin(self.angle))

    @pyqtSlot(QPoint)
    def on_positionChanged(self, pos):
        self.x = pos.x()-415
        self.y = pos.y()-415





