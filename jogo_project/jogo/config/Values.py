import pygame as py

class Values:

        #window
        window_width=1300
        window_height=800


        #menu ------------------------------------------------------
        background="jogo_project/jogo/asset/background/background_menu.png"
        sound_up_white="jogo_project/jogo/asset/icons/volume_up_white.png"
        sound_off_white="jogo_project/jogo/asset/icons/volume_off_white.png"
        esc="jogo_project/jogo/asset/icons/esc_white.png"
        help_move="jogo_project/jogo/asset/background/help_move.png"
        help_interact="jogo_project/jogo/asset/background/help_interact.png"
        sound_menu="jogo_project/jogo/asset/sound/sound_menu.wav"

        #background efect
        alpha=150

        #game name
        name_game="OBLIVION"
        size_name=100
        position_x_name=650
        position_y_name=280

        #text buttons
        text_buttom_star="START"
        text_buttom_exit="EXIT"
        text_buttom_como_jogar="HOW TO PLAY"
        size_text=40

        #title help
        title_help_move="MOVE"
        title_help_interact="INTERACT"
        position_x_title_help_move=300
        position_x_title_help_interact=1000
        position_y_title_help=180

        #texts help
        text_help_move_w="W = move up"
        text_help_move_a="A =  move left"
        text_help_move_s="S =  move down"
        text_help_move_d="D = move right"
        text_help_mode_interact="left mouse button"
        text_help_result_win="Win = find a survivor before time runs out and interact with them"
        text_help_result_lose="Lose = time running out before finding and interacting with the survivor"
        text_help_align="left"
        size_title_help=50
        size_text_help=30
        position_x_text_help=350
        position_y_text_help_move_w=235
        position_y_text_help_move_a=285
        position_y_text_help_move_s=335
        position_y_text_help_move_d=385
        position_x_text_help_interact=1000
        position_x_text_help_result=100
        position_y_text_help_result_win=550
        position_y_text_help_result_lose=600

        #buttons
        position_x_buttons=650
        position_y_buttom_start=420
        position_y_buttom_how_play=520
        position_y_buttom_exit=620
        color=(200, 200, 200)
        color_buttom=(40, 40, 40)
        color_over=(70, 70, 70, 0)
        width_buttom=250
        height_buttom=70
        radius=10

        #buttons circle
        position_x_buttons_circle=1200
        position_y_buttons_circle=100
        width_buttom_circle=50
        height_buttom_circle=50
        radius_circle=50
        padding_buttom=7
        over_add_width=5
        over_add_height=5

        #images help
        size_image_help=(200, 250)
        radius_image_help=10


        #game ------------------------------------------------------
        status="playing"
        status_win="win"
        status_lose="lose"
        fps=60

        #sound
        sound_game="jogo_project/jogo/asset/sound/sound_wind.wav"

        #map
        img_map="jogo_project/jogo/asset/background/background_map.png"
        width_map=6000
        height_map=4461
        size_map=(width_map, height_map)

        #camera
        position_x_camera=0
        position_y_camera=0
        speed_camera=4

        #Player
        position_x_player=0
        position_y_player=4400
        width_player=200
        height_player=200

        #npc
        position_x_npc=3600
        position_y_npc=500
        width_npc=200
        height_npc=200

        #timer
        duration_timer=301
        color_timer=(40, 40, 40)
        color_number_timer=(200, 200, 200)
        size_number_timer=50
        position_x_timer=650
        position_y_timer=100
        width_timer=270
        height_timer=70
        radius_timer=10

        #result win
        text_win="VOCÊ ENCONTROU O SOBREVIVENTE!"
        width_win=window_width
        height_win=window_height
        size_text_win=50
        color_text_win=(200, 200, 200)

        #result lose
        text_lose="VOCÊ MORREU!"
        width_lose=window_width
        height_lose=window_height
        size_text_lose=50
        color_text_lose=(200, 200, 200)
