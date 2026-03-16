import pygame as py
from jogo.entity.Entity import Entity
from jogo.animation.Player_Animation import Player_animation


class Player(Entity):

    def __init__(
        self,
        position_x: int,
        position_y: int,
        width: int,
        height: int):

        super().__init__(
            position_x,
            position_y,
            width,
            height)

        self.anim = Player_animation()
        self.hitbox = py.Rect(position_x, position_y, 70, 112)
        self.sprite_offset_y = -2

    def update(self, dx, dy):
        if dx > 0:
            self.anim.set("run")

        elif dx < 0:
            self.anim.set("run_left")

        elif dy != 0:
            self.anim.set("run")

        else:
            self.anim.set("idle")

        super().update()
        self.rect.centerx = self.hitbox.centerx
        self.rect.bottom = self.hitbox.bottom + self.sprite_offset_y

    def draw(self, screen, cam_x, cam_y):
        super().draw(screen, cam_x, cam_y)