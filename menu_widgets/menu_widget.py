from tkinter import BaseWidget

from PyQt5.QtCore import QTimer, pyqtSlot, QPoint, QUrl, QDir
from PyQt5.QtGui import QPixmap, QPainter, QColor
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel
import random
from game_levels.level1_river import Level1
from game_levels.level2_river import Level2
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
        
        self.main_window = main_window
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.label = QLabel()
        self.label.setPixmap(QPixmap("resources/zuma_menu.png"))
        self.layout.addWidget(self.label)
        self.random_color_manager = RandomColorManager()

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
            LevelButton(100,100,"resources/text_1.png", self.start_level_1)
        ]

    @pyqtSlot(QPoint)
    def on_positionChanged(self, pos):
        for i in self.buttons:
            x,y,w,h = i.get_geometry()
            if pos.x()>x and pos.x()<x+w and pos.y() > y and pos.y() < y+h:
                i.is_pressed = True
            else:
                i.is_pressed = False
    def handle_timer(self):
        self.label.setPixmap(QPixmap("resources/zuma_menu.png"))
        self.qp = QPainter(self.label.pixmap())
        self.paint_buttons()
        self.paint_balls()
        self.move_balls()
        self.qp.end()
        self.update()
    def mousePressEvent(self, a0):
        for i in self.buttons:
            if i.is_pressed:
                i.on_click()

    def start_level_1(self):
        self.main_window.setCentralWidget(GameWidget(
            Level2()
        ))
    def select_level(self):
        print("dsf")
        self.buttons = self.level_buttons

    def move_balls(self):
        rnd = random.randint(0,10)
        if rnd == 10:
            rnd2 = random.randint(200,1400)
            self.balls.append(MenuBall(rnd2,-200, self.random_color_manager.get_random_color()))
        for i in self.balls:
            if i.x < -50:
                self.balls.remove(i)
            i.tick()
    def paint_balls(self):
        for i in self.balls:
            self.qp.setBrush(QColor(i.color))
            self.qp.drawEllipse(i.x,i.y,40,40)
    def paint_buttons(self):
        for i in self.buttons:
            x,y,w,h = i.get_geometry()
            self.qp.drawPixmap(x, y, w, h, QPixmap(i.get_pixmap()))
            self.qp.drawPixmap(x,y,w,h,QPixmap(i.text_resource))


