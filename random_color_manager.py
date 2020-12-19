import random

from PyQt5.QtGui import QColor


class RandomColorManager:
    def get_random_color(self):
        colors = ['red','blue','green', 'yellow']
        return random.choice(colors)
    def get_qt_color_from_string(self, string):
        return QColor(string)