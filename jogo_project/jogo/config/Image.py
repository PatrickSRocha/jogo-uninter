import pygame as py

class Image:

    def __init__(
            self,
            img:py.Surface,
            surface,
            rect,
            size:tuple[int, int],
            radius:int=0):

        self.img=img
        self.surface=surface
        self.rect=rect
        self.size=size
        self.radius=radius

    def draw(self):
        scale = py.transform.scale(self.img, self.size)
        rect = scale.get_rect(center=self.rect.center)
        self.surface.blit(scale, rect)
