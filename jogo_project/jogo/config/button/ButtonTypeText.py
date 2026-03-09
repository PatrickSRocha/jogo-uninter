import pygame as py
from jogo.config.Text import Text
from jogo.config.button.Button import Button

class ButtonTypeText(Button):

    def __init__(
            self,
            text:str,
            color_button:tuple[int,int,int],
            color_text:tuple[int,int,int],
            color_over:tuple[int,int,int],
            size_text:int,
            position_x:int,
            position_y:int,
            width:int,
            height:int,
            radius:int=0,
            align_text:str="center"):

        super().__init__(
                color_button,
                width,
                height,
                position_x,
                position_y,
                radius)

        self.text=text
        self.color_text=color_text
        self.color_over=color_over
        self.size_text=size_text
        self.align_text=align_text
        
        self.tx = Text(
            text=self.text,
            size=self.size_text,
            color=self.color_text,
            width=self.rect.centerx,
            height=self.rect.centery,
            align=self.align_text
        )

    def draw(self):
        surface = py.display.get_surface()
        button_color = self.mouse_over()
        py.draw.rect(surface, button_color, self.rect, border_radius=self.radius)

        self.tx.write()

    def mouse_over(self):
        mouse_position = py.mouse.get_pos()

        if self.rect.collidepoint(mouse_position):
            return self.color_over

        return self.color_button
