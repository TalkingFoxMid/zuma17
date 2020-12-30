import random

from PyQt5.QtCore import QTimer, pyqtSignal, QPoint, pyqtSlot
from PyQt5.QtGui import QPixmap, QPainter, QColor, QMouseEvent, QFont, QPen
from PyQt5.QtWidgets import QWidget, QLabel
from PyQt5.QtWidgets import QGridLayout

from special_providers.angle_provider import AngleProvider
from animation_manager.animation_manager import AnimationManager
from animation_manager.tip_animation import TipAnimation
from special_providers.ball_pixmap_provider import BallPixmapProvider
from special_providers.space_gif_provider import SpaceGifProvider
from task_manager.down_pausa_task import DownPausaTask
from task_manager.task_manager import TaskManager
from task_manager.up_pausa_task import UpPausaTask

from widgets.end_game_win_widget import EndGameWinWidget
from widgets.end_game_lose_widget import EndGameLoseWidget
from game_logic.game_state import GameState
import math

from widgets.menu_button import MenuButton

from widgets.mouse_tracker import MouseTracker
from special_providers.random_color_provider import RandomColorManager
import time


class GameWidget(QWidget):
    """Виджет самой игры"""
    positionChanged = pyqtSignal(QPoint)

    def __init__(self, game_level, main_window, menu_widget):
        self.is_paused = False
        self.TIME_BALL_COLOR = "TIME"
        self.BOOM_BALL_COLOR = "BOOM"
        super().__init__()
        self.space_gif_provider = SpaceGifProvider()
        self.animation_manager = AnimationManager()
        self.ball_pixmap_provider = BallPixmapProvider()
        self.main_window = main_window
        self.menu_widget = menu_widget
        self.angle_provider = AngleProvider()
        self.game_level = game_level
        self.balls_float_animation = 0
        self.pausa_opacity = 0
        self.menu_buttons = [
            MenuButton(200, 400, "resources/kadilo.png", self.back),
            MenuButton(200, 600, "resources/zavarudo.png", self.pause),

        ]
        self.buttons = self.menu_buttons
        self.task_manager = TaskManager()
        self.x = 1
        self.y = 1
        self.is_meta_menud = False
        self.game_state = GameState(game_level,
                                    RandomColorManager(time.time()))
        self.game_state.set_animation_manager(self.animation_manager)
        self.grid = QGridLayout()
        self.canvas = QPixmap(800, 800)
        self.label = QLabel()
        self.tick = 0
        self.label.setPixmap(self.canvas)
        tracker = MouseTracker(self.label)
        tracker.positionChanged.connect(self.on_position_changed)
        self.grid.addWidget(self.label)
        self.setLayout(self.grid)
        self.animation_manager.add_animation(
            TipAnimation()
        )
        self.timer = QTimer()
        self.timer.timeout.connect(self.handle_timer)
        self.timer.start(40)

    def pause(self):
        self.is_paused = not self.is_paused
        if self.is_paused:
            self.task_manager.add_task(UpPausaTask(self))
        else:
            self.task_manager.add_task(DownPausaTask(self))

    def draw_meta_menus(self):
        if self.is_meta_menud:
            self.draw_menu_buttons()

    def change_meta_menud_state(self):
        self.is_meta_menud = not self.is_meta_menud

    def add_balls_float_parameter(self):
        self.balls_float_animation += 0.2

    def handle_timer(self):
        self.tick += 1
        self.task_manager.task_tick()
        if self.game_state.game_ended_win:
            self.end_game_win()

        if self.game_state.lost:
            self.end_game_lose()

        if not self.is_paused:
            self.add_balls_float_parameter()  # visual effect
            self.game_state.tick()

        self.angle = self.angle_provider.get_angle(self.x, self.y)

        self.draw_game_state()

    def left_click(self):
        self.main_window.setFocus()
        self.game_state.shot_a_ball(self.angle)

    def set_pausa_opacity(self, pausa_opacity):
        self.pausa_opacity = pausa_opacity

    def right_click(self):
        self.game_state.swap_balls()

    def wheel_click(self):
        self.game_state.change_balls()

    def mousePressEvent(self, a0: QMouseEvent) -> None:

        if self.is_meta_menud:
            for i in self.buttons:
                if i.is_pressed:
                    i.on_click()
        if a0.button() == 1:
            self.left_click()
        elif a0.button() == 2:
            self.right_click()
        elif a0.button() == 4:
            self.wheel_click()

    def draw_space(self):
        if self.game_state.time_space_opacity == 0:
            return
        self.qp.setOpacity(self.game_state.time_space_opacity)
        self.qp.drawPixmap(0, 0, 800, 800, QPixmap(
            self.space_gif_provider.get_res(self.tick))
                           )
        self.qp.setOpacity(1)

    def draw_game_state(self):
        self.label.setPixmap(QPixmap(self.game_level.map_resource))

        self.qp = QPainter(self.label.pixmap())
        self.draw_space()
        self.qp.setFont(QFont("arial", 22))
        self.draw_central_frog()
        self.draw_conveyor_balls()
        self.draw_flying_balls()
        self.draw_score()
        self.animation_manager.draw_animations(self.qp)
        self.draw_meta_menus()
        self.draw_pausa()
        self.draw_super_balls()

        self.qp.end()
        self.update()

    def draw_menu_buttons(self):
        self.draw_buttons(self.menu_buttons)

    def draw_buttons(self, buttons):
        for i in buttons:
            x, y, w, h = i.get_geometry()
            self.qp.drawPixmap(x, y, w, h, QPixmap(i.get_pixmap()))
            self.qp.drawPixmap(x, y, w, h, QPixmap(i.text_resource))

    def draw_super_balls(self):
        self.qp.setOpacity(0.4)
        if self.game_state.frog_operator.boom_ball_available:
            self.qp.drawPixmap(100, 600, 200, 200,
                               QPixmap("resources/boom.png"))
        if self.game_state.frog_operator.time_ball_available:
            self.qp.drawPixmap(500, 600, 200, 200,
                               QPixmap("resources/time_stop.png"))
        self.qp.setOpacity(1)

    def push_time_ball_get(self):
        self.game_state.frog_operator.get_time_ball()

    def push_boom_ball_get(self):
        self.game_state.frog_operator.get_boom_ball()

    def draw_score(self):
        self.qp.setPen(QColor(0, 0, 0))
        x, y = self.game_level.score_position
        self.qp.drawText(x, y, str(self.game_state.score))

    def get_boom_ball(self):
        self.game_state.frog_operator.first_ball_color = self.BOOM_BALL_COLOR

    def get_time_ball(self):
        self.game_state.frog_operator.first_ball_color = self.TIME_BALL_COLOR

    def draw_flying_balls(self):
        bpp = self.ball_pixmap_provider

        for i in self.game_state.balls:
            if i.must_been_deleted:
                continue
            self.qp.drawPixmap(i.x - 21,
                               i.y - 21,
                               42,
                               42,
                               bpp.get_pixmap(i.color))

    def draw_conveyor_balls(self):
        bpp = self.ball_pixmap_provider
        for i in self.game_state.balls_conveyor.get_balls_list():
            x, y = self.game_state.balls_conveyor.get_ball_position(i)

            self.qp.drawPixmap(x - i.diameter / 2, y - i.diameter / 2,
                               i.diameter,
                               i.diameter,
                               bpp.get_pixmap(i.color))

    def draw_pausa(self):
        if self.pausa_opacity <= 0:
            return
        self.qp.setOpacity(self.pausa_opacity)

        self.qp.drawPixmap(150, 100, 312 * 1.5, 180 * 1.5,
                           QPixmap("resources/pausa_png.png"))
        self.qp.setOpacity(1)

    def draw_central_frog(self):
        bpp = self.ball_pixmap_provider

        self.qp.setPen(QPen(QColor("black"), 3))
        x, y = self.game_level.frog_position
        self.qp.drawPixmap(x - 35, y - 50, QPixmap("resources/frog.png"))
        p = self.game_state.frog_operator.balls_swap_parameter
        p2 = self.game_state.frog_operator.balls_swap_parameter2
        p3 = 1 - self.game_state.frog_operator.balls_swap_parameter3
        self.qp.drawPixmap(x + 40 * p,
                           y - 60 * p,
                           p3 * (42 - 21 * p),
                           p3 * (42 - 21 * p),
                           bpp.get_pixmap(
                               self.game_state.frog_operator.first_ball_color))

        self.qp.drawPixmap(x + 40 - 80 * p,
                           y - 60 + 10 * math.sin(self.balls_float_animation),
                           p3 * 21,
                           p3 * 21,
                           bpp.get_pixmap(
                               self.game_state.frog_operator.
                               second_ball_color))

        self.qp.drawPixmap(x - 40 + 40 * p2,
                           y - 60 + 60 * p2 + 10 * math.sin(
                               self.balls_float_animation),
                           p3 * (21 - 21 * p + 42 * p2),
                           p3 * (21 - 21 * p + 42 * p2),
                           bpp.get_pixmap(
                               self.game_state.frog_operator.third_ball_color))
        if self.game_state.frog_operator.change_balls_cooldown > 0:
            self.qp.drawText(x, y + 80,
                             str(
                                 int(self.game_state.frog_operator.
                                     change_balls_cooldown / 25)
                             ))
        self.qp.drawLine(x + 15, y + 15, x + 15 + 100 * math.cos(self.angle),
                         y + 15 + 100 * math.sin(self.angle))

    def back(self):
        self.main_window.setCentralWidget(type(self.main_window)())

    def end_game_win(self):
        self.main_window.setCentralWidget(EndGameWinWidget(
            self.main_window,
            self.menu_widget,
            self.game_state.score,
            self.game_level.number

        ))

    def end_game_lose(self):
        self.main_window.setCentralWidget(
            EndGameLoseWidget(self.main_window,
                              self.menu_widget)
        )

    @pyqtSlot(QPoint)
    def on_position_changed(self, pos):
        for i in self.buttons:
            x, y, w, h = i.get_geometry()
            if x < pos.x() < x + w and y < pos.y() < y + h:
                i.is_pressed = True

            else:
                i.is_pressed = False
        self.x = pos.x() - 415
        self.y = pos.y() - 415
