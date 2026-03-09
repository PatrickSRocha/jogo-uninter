import pygame as py
from jogo.config.button.Button import Button
from jogo.config.Image import Image

class ButtonTypeImage(Button):

    def __init__(
            self,
            color_button:tuple[int,int,int],
            width:int,
            height:int,
            position_x:int,
            position_y:int,
            image_on:py.Surface,
            image_off:py.Surface,
            padding:int=0,
            add_width:int=0,
            add_height:int=0,
            radius:int=0):

        super().__init__(
                color_button,
                width,
                height,
                position_x,
                position_y,
                radius)

        self.image_on=image_on
        self.image_off=image_off
        self.padding=padding
        self.add_width=add_width
        self.add_height=add_height
        self.img_width=self.width - (self.padding * 2)
        self.img_height=self.height - (self.padding * 2)

    def draw(self):
        surface = py.display.get_surface()
        py.draw.rect(surface, self.color_button, self.rect, border_radius=self.radius)

        if self.state:
            image = self.image_off

        else:
            image = self.image_on

        over=self.mouse_over(self.img_width, self.img_height)

        img = Image(
            img=image,
            surface=surface,
            rect=self.rect,
            size=over)

        img.draw()

    def mouse_over(self, width, height):
        mouse_position = py.mouse.get_pos()

        if self.rect.collidepoint(mouse_position):
            return (width + self.add_width, height + self.add_height)

        return (width, height)
