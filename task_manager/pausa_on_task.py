class PausaOnTask:
    def __init__(self, game_widget):
        self.game_widget = game_widget
        self.remain = 50

    def tick(self):
        self.remain -= 1
        if self.remain <= 0:
            return
        self.game_widget.set_pausa_opacity(
            self.get_pausa_opacity()
        )

    def get_pausa_opacity(self):
        r = 50 -self.remain
        if r < 25:
            print(r/25)
            return r/25
        return 1

    def get_remain(self):
        return self.remain
