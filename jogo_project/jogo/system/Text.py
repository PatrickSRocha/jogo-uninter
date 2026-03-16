import pygame as py

class Text:

    def __init__(
            self,
            text:str,
            size:int,
            color:tuple[int,int,int],
            width:int,
            height:int,
            align="center"):

        self.text=text
        self.size=size
        self.color=color
        self.width=width
        self.height=height
        self.align=align

    def write(self):
        fonte = py.font.SysFont("franklingothicheavy", self.size)
        render = fonte.render(self.text, True, self.color)

        window = py.display.get_surface()

        rect = render.get_rect()

        if self.align in ["left", "right"]:
            setattr(rect, self.align, self.width)
            rect.centery = self.height

        else:
            setattr(rect, self.align, (self.width, self.height))

        window.blit(render,rect)