class Game(object):
    player_obj = None


class Game_Field(object):
    size = 10
    ship_count = 20
    field = dict()
    def __init__(self, size = 10,ship_count = 20):
        self.size = size
        self.ship_count = ship_count
        for i in range(0,size * size):
            self.field[i] = '[ ]'

    def display(self):
        print('  [0][1][2][3][4][5][6][7][8][9]', end = '')
        for i in range(0,self.size * self.size, 10):
            print()
            print(int(i / 10),end = ' ')
            for j in range(0,self.size):
                print(self.field[i + j],end = '')
        

class BaseShip(object):
    belong_to_player = None
    location = None
    def __init__(self, size, size_to_place,belong_to_player,location):
        self.size = size
        self.size_to_place = size_to_place 
        self.belong_to_player = belong_to_player
        self.location = location