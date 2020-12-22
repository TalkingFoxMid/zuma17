import math
from functools import partial


from PyQt5.QtCore import QTimer, pyqtSlot, QPoint, QUrl, QDir
from PyQt5.QtGui import QPixmap, QPainter, QColor, QMouseEvent
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel
import random

from ball_pixmap_provider import BallPixmapProvider
from game_levels.level0_menu import Level0
from game_levels.level1_river import Level1
from game_levels.level2_river import Level2
from game_levels.level3_river import Level3
from game_widget import GameWidget
from menu_widgets.MenuSelectWidget import MenuSelectWidget
from menu_widgets.level_button import LevelButton
from menu_widgets.menu_ball import MenuBall
from menu_widgets.menu_button import MenuButton
from mouse_tracker import MouseTracker
from random_color_manager import RandomColorManager


class MenuWidget(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.mouse_last_x = 0
        self.mouse_last_y = 0
        self.ball_offset_x = 0
        self.ball_offset_y = 0
        self.main_window = main_window
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.label = QLabel()
        self.iter = 0
        self.label.setPixmap(QPixmap("resources/zuma_menu.png"))
        self.layout.addWidget(self.label)
        self.random_color_manager = RandomColorManager()
        self.ball_pixmap_provider = BallPixmapProvider()
        tracker = MouseTracker(self.label)
        tracker.positionChanged.connect(self.on_positionChanged)
        self.timer = QTimer()
        self.timer.timeout.connect(self.handle_timer)
        self.timer.start(40)
        self.balls = []
        self.buttons_main_menu = [
            MenuButton(199,424, "resources/play.png", self.select_level)
        ]
        self.buttons = self.buttons_main_menu
        self.level_buttons = [
            LevelButton(100,100,"resources/text_1.png", partial(self.start_level, Level1)),
            LevelButton(300, 100, "resources/text_2.png", partial(self.start_level, Level2)),
            LevelButton(500, 100, "resources/text_3.png", partial(self.start_level, Level3))
        ]

    @pyqtSlot(QPoint)
    def on_positionChanged(self, pos):
        self.mouseMoveBalls(pos)
        for i in self.buttons:
            x,y,w,h = i.get_geometry()
            if pos.x()>x and pos.x()<x+w and pos.y() > y and pos.y() < y+h:
                i.is_pressed = True
            else:
                i.is_pressed = False
    def handle_timer(self):
        self.iter += 0.1
        self.label.setPixmap(QPixmap(800, 800))
        self.qp = QPainter(self.label.pixmap())
        self.qp.drawPixmap(-100+self.ball_offset_x,
                           -100+self.ball_offset_y,
                           1200+self.ball_offset_x*4+self.ball_offset_y*4,
                           1200+self.ball_offset_x*4+self.ball_offset_y*4,
                           QPixmap("resources/zuma_menu.png"))

        self.paint_buttons()
        self.paint_balls()
        self.move_balls()
        self.draw_frog()

        self.qp.end()
        self.update()
    def draw_frog(self):
        s1 = math.sin(self.iter)
        s2 = math.sin(self.iter+2*math.pi/3)
        s3 = math.sin(self.iter+4*math.pi/3)
        c1 = math.cos(self.iter)
        c2 = math.cos(self.iter+2*math.pi/3)
        c3 = math.cos(self.iter+4*math.pi/3)


        self.qp.drawPixmap(555,555,250,250,QPixmap("resources/metasploit.png"))

        self.qp.drawPixmap(630,630,100,100,QPixmap("resources/frog.png"))
        self.qp.drawPixmap(660+80*s1, 660+80*c1, 42, 42, QPixmap("resources/red_ball.png"))
        self.qp.drawPixmap(660+80*s2,660+80*c2,42,42,QPixmap("resources/blue_ball.png"))
        self.qp.drawPixmap(660+80*s3,660+80*c3,42,42,QPixmap("resources/green_ball.png"))

    def mousePressEvent(self, a0):
        for i in self.buttons:
            if i.is_pressed:
                i.on_click()

    def start_level(self, level):
        self.main_window.setCentralWidget(GameWidget(
            level(),
            self.main_window,
            self
        ))


    def select_level(self):
        self.buttons = self.level_buttons

    def move_balls(self):
        rnd = random.randint(0,10)
        if rnd >7:
            rnd2 = random.randint(200,1400)
            self.balls.append(MenuBall(rnd2,-200, self.random_color_manager.get_random_color(), -10, 10))
            self.balls.append(MenuBall(rnd2-400, 1000, self.random_color_manager.get_random_color(), 10, -10))
        for i in self.balls:
            if i.x < -300 or i.x > 1100 or i.y < -300 or i.y > 1100:
                self.balls.remove(i)
        for i in self.balls:
            i.tick()
            for j in self.balls:
                if i == j:
                    continue
                if self.is_collide(i, j):
                    dx = i.x - j.x
                    dy = i.y - j.y
                    i.speed_x = dx*0.2
                    i.speed_y = dy*0.2
                    j.speed_x = -dx*0.2
                    j.speed_y = -dy*0.2
    def is_collide(self, ball1, ball2):
        dx = ball1.x - ball2.x
        dy = ball1.y - ball2.y
        if abs(dx) > 42:
            return False
        if abs(dy) > 42:
            return False
        if math.sqrt(dx*dx+dy*dy) > 42:
            return False
        return True
    def paint_balls(self):
        for i in self.balls:
            self.qp.drawPixmap(i.x-21-self.ball_offset_x,i.y-21-self.ball_offset_y,42,42, self.ball_pixmap_provider.get_pixmap(i.color))
    def paint_buttons(self):
        for i in self.buttons:
            x,y,w,h = i.get_geometry()
            self.qp.drawPixmap(x, y, w, h, QPixmap(i.get_pixmap()))
            self.qp.drawPixmap(x,y,w,h,QPixmap(i.text_resource))
    def mouseMoveBalls(self, a0):
        dx = (self.mouse_last_x - a0.x())*0.03
        dy = (self.mouse_last_y - a0.y())*0.03
        self.mouse_last_x = a0.x()
        self.mouse_last_y = a0.y()
        if dx == -a0.x() or dy == -a0.y():
            return
        self.ball_offset_x += dx
        self.ball_offset_y += dy
        if self.ball_offset_x > 500:
            self.ball_offset_x = 500
        if self.ball_offset_x < -500:
            self.ball_offset_x = -500
        if self.ball_offset_y > 500:
            self.ball_offset_y = 500
        if self.ball_offset_y < -500:
            self.ball_offset_y = -500

