from jogo.core.Menu import Menu
from jogo.core.Game import Game

class Main:

    def __init__(self):
        running = True

        while running:
            result_menu = Menu().run()

            if result_menu == "quit":
                break

            result_game = Game().run()

            if result_game == "quit":
                break

Main()