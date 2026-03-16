import pygame as py
from jogo.system.Text import Text

class Result:

    def __init__(
            self,
            text:str,
            screen_width:int,
            screen_height:int,
            size:int,
            color:tuple[int,int,int]):

        self.text = text
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.size = size
        self.color = color

        self.text = Text(
            text=self.text,
            size=self.size,
            color=self.color,
            width=self.screen_width // 2,
            height=self.screen_height // 2,
            align="center")

    def draw(self):
        self.text.write()