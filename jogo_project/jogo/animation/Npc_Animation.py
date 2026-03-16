import pygame as py
from jogo.config.Values import Values
from jogo.animation.Animation import Animation

class Npc_animation:

    def __init__(self):

        self.animations={}

        idle=py.image.load(Values.npc_idle).convert_alpha()
        wave=py.image.load(Values.npc_wave).convert_alpha()

        self.animations["idle"] = Animation(
            image=idle,
            total_frames=6,
            animation_speed=0.1)

        self.animations["wave"] = Animation(
            image=wave,
            total_frames=11,
            animation_speed=0.1)

        self.current = "idle"

    def set(self, name):
        if self.current != name:
            self.current = name
            self.animations[name].index = 0

    def update(self):
        self.animations[self.current].update()

    def frame(self):
        return self.animations[self.current].frame()