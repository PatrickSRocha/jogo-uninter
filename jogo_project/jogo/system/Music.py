import pygame as py

class Music:

    def __init__(
            self,
            music:py.mixer.Sound):

        self.music=music

    def play(self):
        self.music.play(-1)

    def stop(self):
        self.music.stop()