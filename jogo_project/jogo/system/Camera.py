import pygame as py

class Camera:

    def __init__(
            self,
            player:py.Rect,
            position_x:int=0,
            position_y:int=0,
            screen_width:int=0,
            screen_height:int=0,
            map_width:int=0,
            map_height:int=0):

        self.position_x=position_x
        self.position_y=position_y
        self.screen_width=screen_width
        self.screen_height=screen_height
        self.player=player
        self.map_width=map_width
        self.map_height=map_height

    def update(self):
        self.position_x = self.player.centerx - self.screen_width // 2
        self.position_y = self.player.centery - self.screen_height // 2

        if self.position_x < 0:
            self.position_x = 0

        if self.position_x > self.map_width - self.screen_width:
            self.position_x = self.map_width - self.screen_width

        if self.position_y < 0:
            self.position_y = 0

        if self.position_y > self.map_height - self.screen_height:
            self.position_y = self.map_height - self.screen_height