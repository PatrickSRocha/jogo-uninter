import pygame as py
from jogo.config.Values import Values
from jogo.system.Text import Text
from jogo.system.Music import Music
from jogo.system.Background import Background
from jogo.button.ButtonTypeText import ButtonTypeText
from jogo.button.ButtonTypeImage import ButtonTypeImage
from jogo.system.Map import Map
from jogo.collision.Construction_collision import Construction_collision
from jogo.system.Camera import Camera
from jogo.entity.Player import Player
from jogo.entity.Npc import Npc
from jogo.system.Move import Move
from jogo.system.Timer import Timer
from jogo.core.Result import Result
from jogo.system.Image import Image


class Objects:

       def __init__(self):
        self.window=py.display.set_mode((Values.window_width, Values.window_height))
        self.background=py.image.load(Values.background).convert_alpha()
        self.sound_up=py.image.load(Values.sound_up_white).convert_alpha()
        self.sound_off=py.image.load(Values.sound_off_white).convert_alpha()
        self.help_move=py.image.load(Values.help_move).convert_alpha()
        self.help_interact=py.image.load(Values.help_interact).convert_alpha()
        self.esc=py.image.load(Values.esc).convert_alpha()
        self.sound_menu=py.mixer.Sound(Values.sound_menu)
        self.sound_game=py.mixer.Sound(Values.sound_game)
        self.map_image = py.image.load(Values.img_map)
        self.map_image = py.transform.scale(self.map_image, Values.size_map)
        self.rect_help_move = py.Rect(200, 350, 0, 0)
        self.rect_help_interact = py.Rect(850, 350, 0, 0)

        self.construction_collision = Construction_collision()
        self.collisions = self.construction_collision.collisions

        self.map = Map(self.map_image)

        self.ms_menu = Music(self.sound_menu)

        self.ms_game = Music(self.sound_game)

        self.bg = Background(
            window=self.window,
            image=self.background,
            alpha=Values.alpha)

        self.tx = Text(
            text=Values.name_game,
            size=Values.size_name,
            color=Values.color,
            width=Values.position_x_name,
            height=Values.position_y_name)

        self.tx_move= Text(
            text=Values.title_help_move,
            size=Values.size_title_help,
            color=Values.color,
            width=Values.position_x_title_help_move,
            height=Values.position_y_title_help)

        self.tx_interact= Text(
            text=Values.title_help_interact,
            size=Values.size_title_help,
            color=Values.color,
            width=Values.position_x_title_help_interact,
            height=Values.position_y_title_help)

        self.tx_move_w = Text(
            text=Values.text_help_move_w,
            size=Values.size_text_help,
            color=Values.color,
            width=Values.position_x_text_help,
            height=Values.position_y_text_help_move_w,
            align=Values.text_help_align)

        self.tx_move_a = Text(
            text=Values.text_help_move_a,
            size=Values.size_text_help,
            color=Values.color,
            width=Values.position_x_text_help,
            height=Values.position_y_text_help_move_a,
            align=Values.text_help_align)

        self.tx_move_s = Text(
            text=Values.text_help_move_s,
            size=Values.size_text_help,
            color=Values.color,
            width=Values.position_x_text_help,
            height=Values.position_y_text_help_move_s,
            align=Values.text_help_align)

        self.tx_move_d = Text(
            text=Values.text_help_move_d,
            size=Values.size_text_help,
            color=Values.color,
            width=Values.position_x_text_help,
            height=Values.position_y_text_help_move_d,
            align=Values.text_help_align)

        self.tx_mode_interact = Text(
            text=Values.text_help_mode_interact,
            size=Values.size_text_help,
            color=Values.color,
            width=Values.position_x_text_help_interact,
            height=Values.position_y_text_help_move_w,
            align=Values.text_help_align)

        self.tx_result_win = Text(
            text=Values.text_help_result_win,
            size=Values.size_text_help,
            color=Values.color,
            width=Values.position_x_text_help_result,
            height=Values.position_y_text_help_result_win,
            align=Values.text_help_align)

        self.tx_result_lose = Text(
            text=Values.text_help_result_lose,
            size=Values.size_text_help,
            color=Values.color,
            width=Values.position_x_text_help_result,
            height=Values.position_y_text_help_result_lose,
            align=Values.text_help_align)

        self.img_help_move = Image(
            img=self.help_move,
            surface=self.window,
            rect=self.rect_help_move,
            size=Values.size_image_help,
            radius=Values.radius_image_help)

        self.img_help_interact = Image(
            img=self.help_interact,
            surface=self.window,
            rect=self.rect_help_interact,
            size=Values.size_image_help,
            radius=Values.radius_image_help)

        self.bt_start = ButtonTypeText(
                text=Values.text_buttom_star,
                color_button=Values.color_buttom,
                color_text=Values.color,
                color_over=Values.color_over,
                size_text=Values.size_text,
                position_x=Values.position_x_buttons,
                position_y=Values.position_y_buttom_start,
                width=Values.width_buttom,
                height=Values.height_buttom,
                radius=Values.radius)

        self.bt_how_play = ButtonTypeText(
                text=Values.text_buttom_como_jogar,
                color_button=Values.color_buttom,
                color_text=Values.color,
                color_over=Values.color_over,
                size_text=Values.size_text,
                position_x=Values.position_x_buttons,
                position_y=Values.position_y_buttom_how_play,
                width=Values.width_buttom,
                height=Values.height_buttom,
                radius=Values.radius)

        self.bt_exit = ButtonTypeText(
                text=Values.text_buttom_exit,
                color_button=Values.color_buttom,
                color_text=Values.color,
                color_over=Values.color_over,
                size_text=Values.size_text,
                position_x=Values.position_x_buttons,
                position_y=Values.position_y_buttom_exit,
                width=Values.width_buttom,
                height=Values.height_buttom,
                radius=Values.radius)

        self.bt_sound = ButtonTypeImage(
                image_on=self.sound_up,
                image_off=self.sound_off,
                color_button=Values.color_buttom,
                position_x=Values.position_x_buttons_circle,
                position_y=Values.position_y_buttons_circle,
                width=Values.width_buttom_circle,
                height=Values.height_buttom_circle,
                padding=Values.padding_buttom,
                add_width=Values.over_add_width,
                add_height=Values.over_add_height,
                radius=Values.radius_circle)

        self.bt_esc = ButtonTypeImage(
                image_on=self.esc,
                image_off=self.esc,
                color_button=Values.color_buttom,
                position_x=Values.position_x_buttons_circle,
                position_y=Values.position_y_buttons_circle,
                width=Values.width_buttom_circle,
                height=Values.height_buttom_circle,
                padding=Values.padding_buttom,
                add_width=Values.over_add_width,
                add_height=Values.over_add_height,
                radius=Values.radius_circle)

        self.player = Player(
            position_x=Values.position_x_player,
            position_y=Values.position_y_player,
            width=Values.width_player,
            height=Values.height_player)

        self.npc = Npc(
            position_x=Values.position_x_npc,
            position_y=Values.position_y_npc,
            width=Values.width_npc,
            height=Values.height_npc)

        self.player_mv = Move(
            body=self.player.hitbox,
            character=self.player,
            speed=Values.speed_camera,
            map_width=Values.width_map,
            map_height=Values.height_map)

        self.cam = Camera(
            player=self.player.rect,
            position_x=Values.position_x_camera,
            position_y=Values.position_y_camera,
            screen_width=Values.window_width,
            screen_height=Values.window_height,
            map_width=Values.width_map,
            map_height=Values.height_map)

        self.timer = Timer(
            duration=Values.duration_timer,
            color_timer=Values.color_timer,
            color_number=Values.color_number_timer,
            size_number=Values.size_number_timer,
            position_x=Values.position_x_timer,
            position_y=Values.position_y_timer,
            width=Values.width_timer,
            height=Values.height_timer,
            radius=Values.radius_timer)

        self.win = Result(
            text=Values.text_win,
            screen_width=Values.width_win,
            screen_height=Values.height_win,
            size=Values.size_text_win,
            color=Values.color_text_win)

        self.lose = Result(
            text=Values.text_lose,
            screen_width=Values.width_lose,
            screen_height=Values.height_lose,
            size=Values.size_text_lose,
            color=Values.color_text_lose)