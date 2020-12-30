class SpaceGifProvider:
    """Предоставляет в зависимости от пройденного в главном
    меню количества тиков - состояние гифки"""
    def get_res(self, tick):
        frame = tick % 181

        frame = str(frame)
        if len(frame) < 3:
            frame = (3-len(frame))*"0"+frame
        res = f"resources/space_gif/frame_{frame}_delay-0.03s.gif"

        return res
