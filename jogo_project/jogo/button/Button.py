import pygame as py

class Button:

    def __init__(
            self,
            color_button:tuple[int, int, int],
            width:int,
            height:int,
            position_x:int,
            position_y:int,
            radius:int=0):

        self.rect=py.Rect(0, 0, width, height)
        self.rect.center=(position_x, position_y)
        self.color_button=color_button
        self.width=width
        self.height=height
        self.position_x=position_x
        self.position_y=position_y
        self.radius=radius
        self.state=False
        self.pressed=False

    def draw(self):
        raise NotImplementedError("A subclass must implement draw().")

    def update(self, event):
        if event.type == py.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                self.state = not self.state
                return True

        return False

    def mouse_over(self):
        return False
