from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QKeyEvent
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent, QSound
from PyQt5.QtWidgets import *
import sys

from random_music_provider import RandomMusicProvider
from widgets.end_game_win_widget import EndGameWinWidget
from widgets.game_widget import GameWidget
from widgets.menu_widget import MenuWidget


class MainWindow(QMainWindow):
    BACKSPACE_KEY_ID = 16777216
    ESC_KEY_ID = 16777219
    T_KEY = 84
    B_KEY = 66

    def __init__(self):
        super().__init__()

        random_music_provider = RandomMusicProvider()
        self.url = QUrl.fromLocalFile(random_music_provider.get_random_music())
        self.content = QMediaContent(self.url)
        self.player = QMediaPlayer()
        self.player.setVolume(20)
        self.player.setMedia(self.content)

        self.menu_widget = MenuWidget(self)

        self.player.play()
        self.setCentralWidget(self.menu_widget)
        self.setGeometry(0, 0, 800, 800)

    def keyPressEvent(self, a0: QKeyEvent) -> None:
        if a0.key() == self.T_KEY and isinstance(
                self.centralWidget(),
                GameWidget):
            self.centralWidget().push_time_ball_get()
        if a0.key() == self.B_KEY and isinstance(
                self.centralWidget(),
                GameWidget):
            self.centralWidget().push_boom_ball_get()
        if a0.key() == self.BACKSPACE_KEY_ID and isinstance(
                self.centralWidget(),
                GameWidget):
            self.centralWidget().change_meta_menud_state()
        if isinstance(self.centralWidget(), EndGameWinWidget):
            if a0.key() == self.ESC_KEY_ID:
                self.centralWidget().remove_name_symbol()
                return
            txt = a0.text()
            if len(txt) == 1:
                self.centralWidget().add_name_symbol(txt)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    app.exec_()
