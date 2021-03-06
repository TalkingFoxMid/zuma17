import random

from PyQt5.QtGui import QColor


class RandomColorManager:
    """Получает распределение цветов вида [0,1,2,3],
    массив из 4 чисел, где каждое из чисел означает,
    сколько шариков того или иного цвета сейчас на конвеере.
    В зависимости от этого возвращает случайный шар.
    Если такое распределение не пришло, просто возвращает случайный."""
    def __init__(self, seed):
        self.random = random.Random()
        self.random.seed(seed)

    def get_random_color(self, color_distribution=None):
        colors = ['red', 'blue', 'green', 'yellow']
        if color_distribution is None:
            return self.random.choice(colors)
        elif sum(color_distribution) == 0:
            return self.random.choice(colors)
        else:
            r = color_distribution[0]
            g = color_distribution[1]
            b = color_distribution[2]
            y = color_distribution[3]
            return self.random.choice(r * ['red'] + g * ['blue'] + b * ['green'] + y * ['yellow'])

    def get_qt_color_from_string(self, string):
        return QColor(string)
