import pygame as py
from jogo.config.Values import Values
from jogo.config.Objects import Objects


class Game:

    def __init__(self):
        py.init()
        self.obj = Objects()
        self.screen = py.display.set_mode((Values.window_width, Values.window_height))
        self.state = Values.status

        self.result_time = None
        self.death_time = None

    def run(self):
        clock = py.time.Clock()

        if not self.obj.bt_sound.state:
            self.obj.ms_game.play()

        while True:
            for event in py.event.get():
                if event.type == py.QUIT:
                    self.obj.ms_game.stop()
                    return "quit"

                if self.state == "playing":
                    clicked_sound = self.obj.bt_sound.update(event)
                    if clicked_sound:
                        if self.obj.bt_sound.state:
                            self.obj.ms_game.stop()

                        else:
                            self.obj.ms_game.play()

                if event.type == py.MOUSEBUTTONDOWN and self.state == "playing":
                    mouse_x, mouse_y = py.mouse.get_pos()

                    world_x = mouse_x + self.obj.cam.position_x
                    world_y = mouse_y + self.obj.cam.position_y

                    if self.obj.player.hitbox.colliderect(self.obj.npc.rect):
                        if self.obj.npc.rect.collidepoint(world_x, world_y):
                            if self.obj.timer.time_left() > 0:
                                self.state = "win"
                                self.result_time = py.time.get_ticks()

                if event.type == py.MOUSEBUTTONDOWN and self.state in ("win", "lose"):
                    if py.time.get_ticks() - self.result_time > 500:
                        self.obj.ms_game.stop()
                        return

            if self.state == "playing":
                walls = [c.rect for c in self.obj.collisions]

                dx, dy = self.obj.player_mv.update(walls)

                self.obj.player.update(dx, dy)
                self.obj.npc.update(self.obj.player, self.obj.cam.position_x, self.obj.cam.position_y, Values.window_width, Values.window_height)
                self.obj.cam.update()

                if self.obj.timer.finished:
                    self.obj.ms_game.stop()
                    self.obj.player.anim.set("dead")
                    self.state = "dying"
                    self.death_time = py.time.get_ticks()

            elif self.state == "dying":
                self.obj.player.anim.update()

                if py.time.get_ticks() - self.death_time > 1500:
                    self.state = "lose"
                    self.result_time = py.time.get_ticks()

            self.screen.fill((0, 0, 0))

            if self.state in ("playing", "dying"):
                self.obj.map.draw(self.screen, self.obj.cam.position_x, self.obj.cam.position_y)

                self.obj.timer.draw()
                self.obj.player.draw(self.screen, self.obj.cam.position_x, self.obj.cam.position_y)
                self.obj.npc.draw(self.screen, self.obj.cam.position_x, self.obj.cam.position_y)

                if self.state == "playing":
                    self.obj.bt_sound.draw()

            elif self.state == "win":
                self.obj.win.draw()

            elif self.state == "lose":
                self.obj.lose.draw()

            py.display.flip()

            clock.tick(Values.fps)