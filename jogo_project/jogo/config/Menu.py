import pygame as py
from jogo.config.Text import Text
from jogo.config.Music import Music
from jogo.config.Background import Background
from jogo.config.button.ButtonTypeText import ButtonTypeText
from jogo.config.button.ButtonTypeImage import ButtonTypeImage

class Menu:

    def __init__(self):
        py.init()
        self.width=1000
        self.height=600
        self.window=py.display.set_mode((self.width, self.height))
        self.img_background=py.image.load("jogo_project/jogo/asset/background/backgroundMenu.png")
        self.sound=py.mixer.Sound("jogo_project/jogo/sound/soundMenu.wav")
        self.img_sound=py.image.load("jogo_project/jogo/asset/icons/volume_up_200.png")
        self.img_sound_off=py.image.load("jogo_project/jogo/asset/icons/volume_off_200.png")
        self.img_settings=py.image.load("jogo_project/jogo/asset/icons/settings_200.png")

        self.bg = Background(
            window=self.window,
            image=self.img_background,
            alpha=150)

        self.ms = Music(
            self.sound)

        self.tx = Text(
            text="OBLIVION",
            size=100,
            color=(200, 200, 200),
            width=self.width//2,
            height=self.height//3)

        self.bt_start = ButtonTypeText(
                text="START",
                color_button=(40, 40, 40),
                color_text=(200, 200, 200),
                color_over=(70, 70, 70, 0),
                size_text=50,
                position_x=self.width/2,
                position_y=self.height/1.7,
                width=250,
                height=70,
                radius=10,
                align_text="center")

        self.bt_exit = ButtonTypeText(
                text="EXIT",
                color_button=(40, 40, 40),
                color_text=(200, 200, 200),
                color_over=(70, 70, 70),
                size_text=50,
                position_x=self.width/2,
                position_y=self.height/1.3,
                width=250,
                height=70,
                radius=10,
                align_text="center")
        
        self.bt_sound = ButtonTypeImage(
                image_on=self.img_sound,
                image_off=self.img_sound_off,
                color_button=(40, 40, 40),
                position_x=self.width-150,
                position_y=self.height/10,
                width=50,
                height=50,
                padding=7,
                add_width=5,
                add_height=5,
                radius=50)

        self.bt_config = ButtonTypeImage(
                image_on=self.img_settings,
                image_off=self.img_settings,
                color_button=(40, 40, 40),
                position_x=self.width-70,
                position_y=self.height/10,
                width=50,
                height=50,
                padding=7,
                add_width=5,
                add_height=5,
                radius=50)

    def run(self):
        py.init()
        self.ms.play()
        self.bg.draw()
        self.tx.write()
        self.bt_start.draw()
        self.bt_exit.draw()
        self.bt_sound.draw()
        self.bt_config.draw()
        py.display.flip()
        self.menu_persistence()

    def menu_persistence(self):
        while True:
            for event in py.event.get():
                if event.type == py.QUIT:
                    py.quit()
                    quit()

            clicked_sound = self.bt_sound.update()
            if clicked_sound:
                if self.bt_sound.state:
                    self.ms.stop()
                else:
                    self.ms.play()

            clicked_exit = self.bt_exit.update()
            if clicked_exit:
                    py.quit()
                    quit()

            self.bt_start.update()
            self.bt_config.update()

            self.bg.draw()
            self.tx.write()
            self.bt_start.draw()
            self.bt_exit.draw()
            self.bt_sound.draw()
            self.bt_config.draw()

            py.display.flip()