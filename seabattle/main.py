import gamefield, player
from functools import reduce
game = gamefield.Game_Field(10,20)
game.field[10] = '[X]'
game.field[0] = '[Y]'
game.field[1] = '[o]'
game.field[11] = '[o]'
game.field[20] = '[o]'
game.field[21] = '[o]'

#game.display()
sh1 = gamefield.BaseShip(4, 4, player.Player("Vasya",True))
sh1.set_location()
#l = int(input())
#print(l)