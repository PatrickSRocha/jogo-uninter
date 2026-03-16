import pygame as py
from jogo.animation.Animation import Animation

class Player_animation:

    def __init__(self):

        self.animations={}

        idle=py.image.load("jogo_project/jogo/asset/player/idle.png").convert_alpha()
        run=py.image.load("jogo_project/jogo/asset/player/run.png").convert_alpha()
        run_left=py.image.load("jogo_project/jogo/asset/player/run_left.png").convert_alpha()
        dead=py.image.load("jogo_project/jogo/asset/player/dead.png").convert_alpha()

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