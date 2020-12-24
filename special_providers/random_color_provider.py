import random


class RandomColorManager:
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

