class UpPausaTask:
    def __init__(self, game_widget):
        self.game_widget = game_widget
        self.remain = 10

    def tick(self):
        if self.remain <= 0:
            self.game_widget.set_pausa_opacity(1)
            return
        self.game_widget.set_pausa_opacity(self.get_pausa_opacity())
        self.remain -= 1

    def get_pausa_opacity(self):
        return (10-self.remain)/10

    def get_remain(self):
        return self.remain
