import pygame as py
from jogo.config.Values import Values
from jogo.animation.Animation import Animation

class Player_animation:

    def __init__(self):

        self.animations={}

        idle=py.image.load(Values.player_idle).convert_alpha()
        run=py.image.load(Values.player_run).convert_alpha()
        run_left=py.image.load(Values.player_run_left).convert_alpha()
        dead=py.image.load(Values.player_deade).convert_alpha()

        self.animations["idle"] = Animation(
            image=idle,
            total_frames=7,
            animation_speed=0.1)

        self.animations["run_left"] = Animation(
            image=run_left,
            total_frames=8,
            animation_speed=0.1)

        self.animations["run"] = Animation(
            image=run,
            total_frames=8,
            animation_speed=0.1)

        self.animations["dead"] = Animation(
            image=dead,
            total_frames=4,
            animation_speed=0.04)

        self.current = "idle"

    def set(self, name):
        if self.current != name:
            self.current = name
            self.animations[name].index = 0

    def update(self):
        self.animations[self.current].update()

    def frame(self):
        return self.animations[self.current].frame()