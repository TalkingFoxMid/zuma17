from animation_manager.points_animation import PointsAnimation


class AnimationManager:
    def __init__(self):
        self.animations = []

    def add_animation(self, animation):
        self.animations.append(animation)
    def add_points_animation(self,x,y,points,color):
        self.add_animation(PointsAnimation(
            x, y, points, color
        ))
    def draw_animations(self, qp):
        for i in self.animations:
            if i.ended:
                self.animations.remove(i)
        for i in self.animations:
            i.draw(qp)
            i.tick()
