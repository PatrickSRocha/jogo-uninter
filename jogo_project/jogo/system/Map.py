import pygame as py

class Map:

    def __init__(self, image: py.Surface):
        self.image = image
        self.rect = self.image.get_rect()

    def draw(self, screen, camera_x, camera_y):
        screen.blit(self.image, (-camera_x, -camera_y))