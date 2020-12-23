from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QKeyEvent
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtWidgets import *
import sys

from end_game_win_widget import EndGameWinWidget
from game_widget import GameWidget
from menu_widgets.menu_widget import MenuWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.url = QUrl.fromLocalFile("resources/music.mp3")
        self.content = QMediaContent(self.url)
        self.player  =QMediaPlayer()
        self.player.setMedia(self.content)
        self.player.play()
        self.menu_widget = MenuWidget(self)
        self.setCentralWidget(self.menu_widget)
        self.setGeometry(0, 0, 800, 800)
    def keyPressEvent(self, a0: QKeyEvent) -> None:
        if a0.key() == 16777216 and isinstance(self.centralWidget(), GameWidget):
            self.centralWidget().change_meta_menud_state()
        if isinstance(self.centralWidget(), EndGameWinWidget):
            if a0.key() == 16777219:
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