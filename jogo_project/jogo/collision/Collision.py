import pygame as py

class Collision:

    def __init__(
            self,
            x:int,
            y:int,
            w:int,
            h:int):

        self.rect = py.Rect(x, y, w, h)

    def draw(self, screen, cam_x, cam_y):
        py.draw.rect(screen, (255, 0, 0),
            (
                self.rect.x - cam_x,
                self.rect.y - cam_y,
                self.rect.width,
                self.rect.height
            ),
            2 
        )