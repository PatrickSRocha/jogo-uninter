import pygame as py

class Entity:

    def __init__(
            self,
            position_x:int,
            position_y:int,
            width:int,
            height:int):

        self.rect = py.Rect(position_x, position_y, width, height)
        self.anim = None

    def draw(self, screen, cam_x, cam_y):
        frame = self.anim.frame()
        scale = py.transform.scale(frame,(self.rect.w, self.rect.h))
        screen.blit(scale, (self.rect.x - cam_x, self.rect.y - cam_y))

    def update(self):
        self.anim.update()
