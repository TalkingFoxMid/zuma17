import random


class RandomMusicProvider:
    music_list = ["music.mp3"]

    def get_random_music(self):
        return "resources/" + random.choice(self.music_list)
