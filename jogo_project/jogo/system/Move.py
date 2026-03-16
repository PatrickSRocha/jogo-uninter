import pygame as py

class Move:

    def __init__(
            self,
            body,
            character,
            speed,
            map_width,
            map_height):

        self.body = body
        self.character = character
        self.speed = speed
        self.map_width = map_width
        self.map_height = map_height

    def move(self):
        keys = py.key.get_pressed()

        dx = 0
        dy = 0

        if keys[py.K_a]:
            dx = -self.speed

        if keys[py.K_d]:
            dx = self.speed

        if keys[py.K_w]:
            dy = -self.speed

        if keys[py.K_s]:
            dy = self.speed

        return dx, dy

    def move_x(self, dx, walls):
        self.body.x += dx

        for wall in walls:
            if self.body.colliderect(wall):
                if dx > 0:
                    self.body.right = wall.left

                if dx < 0:
                    self.body.left = wall.right

    def move_y(self, dy, walls):
        self.body.y += dy

        for wall in walls:
            if self.body.colliderect(wall):
                if dy > 0:
                    self.body.bottom = wall.top

                if dy < 0:
                    self.body.top = wall.bottom

    def inside_map(self):
        if self.body.left < 0:
            self.body.left = 0

        if self.body.right > self.map_width:
            self.body.right = self.map_width

        if self.body.top < 0:
            self.body.top = 0

        if self.body.bottom > self.map_height:
            self.body.bottom = self.map_height

    def update(self, walls):
        dx, dy = self.move()
        
        self.move_x(dx, walls)
        self.move_y(dy, walls)
        
        self.inside_map()

        return dx, dy