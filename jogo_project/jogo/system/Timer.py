import pygame as py
from jogo.system.Text import Text


class Timer:

    def __init__(
            self,
            duration:int,
            color_timer:tuple[int, int, int],
            color_number:tuple[int, int, int],
            size_number:int,
            position_x:int,
            position_y:int,
            width:int,
            height:int,
            radius:int=0,
            align_number="center"):

        self.duration = duration * 1000
        self.start_time = py.time.get_ticks()
        self.finished = False

        self.rect = py.Rect(0, 0, width, height)
        self.rect.center = (position_x, position_y)

        self.color_timer = color_timer
        self.radius = radius

        self.text = Text(
            text="",
            size=size_number,
            color=color_number,
            width=self.rect.centerx,
            height=self.rect.centery,
            align=align_number
        )

    def reset(self):
        self.start_time = py.time.get_ticks()
        self.finished = False

    def time_left(self):
        now = py.time.get_ticks()
        remaining = self.duration - (now - self.start_time)

        if remaining <= 0:
            remaining = 0
            self.finished = True

        return remaining // 1000

    def draw(self):
        remaining = self.time_left()

        minutes = remaining // 60
        seconds = remaining % 60

        self.text.text = f"{minutes:02}:{seconds:02}"

        surface = py.display.get_surface()
        py.draw.rect(surface, self.color_timer, self.rect, border_radius=self.radius)

        self.text.width = self.rect.centerx
        self.text.height = self.rect.centery

        self.text.write()