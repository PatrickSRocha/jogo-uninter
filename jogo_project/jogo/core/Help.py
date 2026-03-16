import pygame as py
from jogo.config.Values import Values

class Help:

    def __init__(self, obj):
        self.obj = obj
        py.time.wait(120)

    def run(self):
        clock = py.time.Clock()

        while True:
            for event in py.event.get():
                if event.type == py.QUIT:
                    py.quit()
                    quit()

                if self.obj.bt_esc.update(event):
                    return

            self.draw()

            py.display.flip()

            clock.tick(Values.fps)

    def draw(self):
        surface = py.display.get_surface()

        overlay = py.Surface(surface.get_size())
        overlay.set_alpha(200)
        overlay.fill((0,0,0))

        surface.blit(overlay,(0,0))

        self.obj.bt_esc.draw()
        self.obj.tx_move.write()
        self.obj.tx_interact.write()
        self.obj.tx_move_w.write()
        self.obj.tx_move_a.write()
        self.obj.tx_move_s.write()
        self.obj.tx_move_d.write()
        self.obj.tx_mode_interact.write()
        self.obj.tx_result_win.write()
        self.obj.tx_result_lose.write()
        self.obj.img_help_move.draw()
        self.obj.img_help_interact.draw()