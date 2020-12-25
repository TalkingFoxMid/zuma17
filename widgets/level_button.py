class LevelButton:
    def __init__(self, left, up, text_resource, on_click):
        self.left = left
        self.up = up
        self.on_click = on_click
        self.width = 200
        self.height = 150
        self.is_pressed = False
        self.hidden = False
        self.text_resource = text_resource

    def get_geometry(self):
        return [self.left, self.up, self.width, self.height]

    def get_pixmap(self):
        if self.is_pressed:
            return "resources/level_button2.png"
        else:
            return "resources/level_button.png"
