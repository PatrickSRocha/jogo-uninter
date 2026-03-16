import pygame as py
from jogo.entity.Entity import Entity
from jogo.animation.Npc_Animation import Npc_animation

class Npc(Entity):

    def __init__(
        self,
        position_x:int,
        position_y:int,
        width:int,
        height:int):

        super().__init__(
            position_x,
            position_y,
            width,
            height)

        self.anim=Npc_animation()
        self.dialogue_active = False

    def wave_player(self, cam_x, cam_y, screen_w, screen_h):
        camera_rect = py.Rect(cam_x, cam_y, screen_w, screen_h)
        return self.rect.colliderect(camera_rect)

    def player_touching(self, player):
        return self.rect.colliderect(player.hitbox)

    def player_click(self, player):
        mouse_click = py.mouse.get_pressed()[0]

        if mouse_click and self.player_touching(player):
            self.dialogue_active = True

    def update(self, player, cam_x, cam_y, screen_w, screen_h):
        self.player_click(player)

        if self.dialogue_active:
            self.anim.set("idle")

        elif self.wave_player(cam_x, cam_y, screen_w, screen_h):
            self.anim.set("wave")

        else:
            self.anim.set("idle")

        super().update()
