from PyQt5.QtGui import QPixmap


class BallPixmapProvider:
    def __init__(self):
        self.pixmap_dictionary = {
            "red": QPixmap("resources/red_ball.png"),
            "green": QPixmap("resources/green_ball.png"),
            "blue": QPixmap("resources/blue_ball.png"),
            "yellow": QPixmap("resources/yellow_ball.png"),
        }
    def get_pixmap(self, color):
        return self.pixmap_dictionary[color]