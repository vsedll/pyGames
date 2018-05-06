
class Player(object):
    #turn = False
    #name = Player1
    ships = None
    def __init__(self, name,first_turn):
        self.firs_turn = first_turn
        self.name = name
        self.ships = list()

    def to_place_ship(self, ship):
        ship.location = list(input('Введите координаты размещения коробля: '))
        self.ships.append(ship) 

class Shot(object):
    @staticmethod
    def perform(player_name, coords):
        return #miss or hit


