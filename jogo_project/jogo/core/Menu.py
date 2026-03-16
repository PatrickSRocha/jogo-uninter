import pygame as py
from jogo.config.Values import Values
from jogo.config.Objects import Objects
from jogo.core.Help import Help

class Menu:

    def __init__(self):
        py.init()
        self.obj = Objects()

    def run(self):
        self.obj.ms_menu.play()
        self.obj.bg.draw()
        self.obj.tx.write()
        self.obj.bt_start.draw()
        self.obj.bt_how_play.draw()
        self.obj.bt_exit.draw()
        self.obj.bt_sound.draw()
        py.display.flip()
        return self.menu_persistence()

    def menu_persistence(self):
        clock = py.time.Clock()

        while True:

            for event in py.event.get():
                if event.type == py.QUIT:
                    return "quit"

                clicked_start = self.obj.bt_start.update(event)
                if clicked_start:
                    self.obj.ms_menu.stop()
                    return

                clicked_how_play = self.obj.bt_how_play.update(event)
                if clicked_how_play:
                    Help(self.obj).run()

                clicked_sound = self.obj.bt_sound.update(event)
                if clicked_sound:
                    if self.obj.bt_sound.state:
                        self.obj.ms_menu.stop()
                    else:
                        self.obj.ms_menu.play()

                clicked_exit = self.obj.bt_exit.update(event)
                if clicked_exit:
                    return "quit"

            self.obj.bg.draw()
            self.obj.tx.write()
            self.obj.bt_start.draw()
            self.obj.bt_how_play.draw()
            self.obj.bt_exit.draw()
            self.obj.bt_sound.draw()

            py.display.flip()

            clock.tick(Values.fps)