import pygame as py

class Animation:

    def __init__(
            self,
            image:py.Surface,
            total_frames:int,
            animation_speed:float=0.1):

        self.frames = []
        self.index = 0
        self.animation_speed = animation_speed

        frame_width = image.get_width() // total_frames
        frame_height = image.get_height()

        for i in range(total_frames):
            rect = py.Rect(i * frame_width, 0, frame_width, frame_height)
            frame = image.subsurface(rect)
            self.frames.append(frame)

    def frame(self):
        return self.frames[int(self.index)]

    def update(self):
        self.index += self.animation_speed

        if self.index >= len(self.frames):
            self.index = 0