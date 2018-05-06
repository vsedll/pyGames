import gamefield, player

game = gamefield.Game_Field(10,20)
game.field[10] = '[X]'
game.field[0] = '[Y]'
game.field[1] = '[o]'
game.field[11] = '[o]'
game.field[20] = '[o]'
game.field[21] = '[o]'

game.display()

