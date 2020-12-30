from animation_manager.boom_animation import BoomAnimation
from animation_manager.points_animation import PointsAnimation


class AnimationManager:
    def __init__(self):
        self.animations = []

    def add_animation(self, animation):
        self.animations.append(animation)

    def draw_animations(self, qp):
        """Отрисовывает все анимации из списка. Удаляет, если они
        закончились. """
        for i in self.animations:
            if i.ended:
                self.animations.remove(i)
        for i in self.animations:
            i.draw(qp)
            i.tick()

    def add_boom_animation(self, x, y):
        self.add_animation(BoomAnimation(x, y))

    def add_points_animation(self, x, y, size, color):
        self.add_animation(PointsAnimation(
            x,
            y,
            size,
            color
        ))
