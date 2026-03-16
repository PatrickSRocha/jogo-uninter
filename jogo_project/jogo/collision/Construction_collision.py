from jogo.collision.Collision import Collision

class Construction_collision:

    def __init__(self):

        #constructions
        self.collisions = [
            Collision(5022, 3310, 864, 790), #bank
            Collision(4760, 1620, 1230, 1150), #hospital
            Collision(2820, 1590, 891, 1220), #church
            Collision(1510, 3315, 590, 528), #market
            Collision(360, 2430, 1194, 700), #train station
            Collision(420, 340, 1080, 840), #school
            Collision(2600, 340, 920, 850), #police station
            Collision(5110, 340, 880, 900), #prefecture

            #houses
            Collision(0, 1615, 1480, 410), #group of houses above the train station
            Collision(410, 3300, 700, 760), #group of houses below the train station
            Collision(2948, 3280, 1525, 780), #group of houses next to the bank
            Collision(1660, 440, 880, 760), #group of houses next to the school

            #grids
            Collision(1965, 2690, 242, 150), #grid font
            Collision(1965, 1590, 27, 1245), #grid left
            Collision(1965, 1590, 900, 141), #grid top

            #walls
            Collision(3500, 340, 1400, 150), #wall top
            Collision(4480, 340, 450, 850), #wall right
            Collision(3500, 1040, 560, 150), #wall bottom

            #huts
            Collision(4380, 480, 200, 350),

            #survivor area
            Collision(3500, 480, 320, 200),

            #tombs
            Collision(1965, 1590, 217, 287), #special tomb 1 row 1 column
            Collision(2380, 1800, 60, 60), #1 row 2 column
            Collision(2680, 1800, 60, 60), #1 row 3 column

            Collision(2040, 2050, 60, 60), #2 row 1 column
            Collision(2360, 2050, 60, 60), #2 row 2 column
            Collision(2720, 2050, 60, 60), #2 row 3 column

            Collision(2040, 2300, 60, 60), #3 row 1 column
            Collision(2360, 2300, 60, 60), #3 row 2 column
            Collision(2730, 2300, 60, 60), #3 row 3 column

            Collision(2060, 2560, 60, 60), #3 row 1 column
            Collision(2370, 2560, 60, 60), #3 row 2 column
            Collision(2710, 2560, 60, 60), #3 row 3 column

            #npc
            Collision(3640, 590, 100, 120)
        ]