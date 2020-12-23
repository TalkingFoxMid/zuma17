class MenuButton:
    def __init__(self, left, up, text_resource, on_click):
        self.left = left
        self.up = up
        self.on_click = on_click
        self.width = 327
        self.height = 106
        self.is_pressed = False

        self.text_resource = text_resource

    def get_geometry(self):
        if not self.is_pressed:
            return [self.left + 36, self.up + 26, self.width, self.height]
        else:
            return [self.left, self.up, self.width + 64, self.height + 50]

    def get_pixmap(self):
        if self.is_pressed:
            return "resources/button_pressed.png"
        else:
            return "resources/button.png"
