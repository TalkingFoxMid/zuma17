class AnimationManager:
    def __init__(self):
        self.animations = []
    def add_animation(self, animation):
        self.animations.append(animation)
    def draw_animations(self, qp):
        for i in self.animations:
            if i.ended:
                self.animations.remove(i)
        for i in self.animations:
            i.draw(qp)
            i.tick()

