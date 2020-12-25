class MenuGifResProvider:
    """Предоставляет в зависимости от пройденного в главном
    меню количества тиков - состояние гифки"""
    def get_res(self, tick):
        tick = int(tick / 2)
        frame = tick % 43

        frame = str(frame)
        if len(frame) == 1:
            frame = "0"+frame
        res = f"resources/menu_gif/frame_{frame}_delay-0.2s.gif"

        return res
