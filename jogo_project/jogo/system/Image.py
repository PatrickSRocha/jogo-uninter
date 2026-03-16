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

    def draw(self, cam_x=0, cam_y=0):
        scale = py.transform.scale(self.img, self.size)
        rect = scale.get_rect(center=(self.rect.centerx - cam_x, self.rect.centery - cam_y))
        self.surface.blit(scale, rect)
