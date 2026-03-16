import pygame as py

class Background:

    def __init__(
            self,
            window,
            image:py.Surface,
            alpha:int=0,
            filter_img:tuple[int,int,int]=(0,0,0)):

        self.window=window
        self.image=image
        self.alpha=alpha
        self.filter_img=filter_img

    def draw(self):
        background = py.transform.scale(self.image, self.window.get_size())

        rect = background.get_rect()
        self.window.blit(background,rect)

        overlay = py.Surface(self.window.get_size())
        overlay.set_alpha(self.alpha)
        overlay.fill(self.filter_img)

        self.window.blit(overlay, (0,0))
