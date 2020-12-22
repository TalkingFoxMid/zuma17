import random

from PyQt5.QtGui import QColor


class RandomColorManager:
    def get_random_color(self, color_distribution=None):
        colors = ['red','blue','green', 'yellow']
        if color_distribution is None:
            return random.choice(colors)
        elif sum(color_distribution) == 0:
            return 'red'
        else:
            r = color_distribution[0]
            g = color_distribution[1]
            b = color_distribution[2]
            y = color_distribution[3]
            return random.choice(r*['red']+g*['blue']+b*['green']+y*['yellow'])
    def get_qt_color_from_string(self, string):
        return QColor(string)