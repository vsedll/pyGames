import random


def X0X_game():

    print("Добро пожаловать в игру крестики и нолики!")
    game_field = {'row1':['_','_','_'], 'row2':['_','_','_'], 'row3':['_','_','_'], 'col1':['_','_','_'], 'col2':['_','_','_'], 'col3':['_','_','_'], 'diag1':['_','_','_'], 'diag2':['_','_','_']}
    player_move = [0,0]
    ai_move = [0,0]
    while (True):        
        print(game_field['row1'])
        print(game_field['row2'])
        print(game_field['row3'])

        while True:
            player_move[0] = int(input("Ваш ход укажите ряд:>"))
            player_move[1] = int(input("Ваш ход укажите столбец:>"))
            if check_oncorrect_move(game_field, player_move):
                break
            else:
                print("Некоректный ход")
        game_field = change_game_field(game_field, player_move, "X")
        if check_game_status(game_field, "X"):
            break

        while True:
            ai_move[0] = random.randint(1,3)
            ai_move[1] = random.randint(1,3)
            if check_oncorrect_move(game_field, ai_move):
                break

        game_field = change_game_field(game_field, ai_move, "0")
        if check_game_status(game_field, "0"):
            break

    print("Поздравляем!")


def change_game_field(game_field, player_move, turn):
    if (player_move[0] == 1) and (player_move[1] == 1):
        game_field['row1'][0] = turn
        game_field['col1'][0] = turn
        game_field['diag1'][0] = turn
    if (player_move[0] == 1) and (player_move[1] == 2):
        game_field['row1'][1] = turn
        game_field['col2'][0] = turn
    if (player_move[0] == 1) and (player_move[1] == 3):
        game_field['row1'][2] = turn
        game_field['col3'][0] = turn
        game_field['diag2'][0] = turn
    
    if (player_move[0] == 2) and (player_move[1] == 1):
        game_field['row2'][0] = turn
        game_field['col1'][1] = turn
    if (player_move[0] == 2) and (player_move[1] == 2):
        game_field['row2'][1] = turn
        game_field['col2'][1] = turn
        game_field['diag1'][1] = turn
        game_field['diag2'][1] = turn
    if (player_move[0] == 2) and (player_move[1] == 3):
        game_field['row2'][2] = turn
        game_field['col3'][1] = turn

    if (player_move[0] == 3) and (player_move[1] == 1):
        game_field['row3'][0] = turn
        game_field['col1'][0] = turn
        game_field['diag2'][2] = turn
    if (player_move[0] == 3) and (player_move[1] == 2):
        game_field['row3'][1] = turn
        game_field['col2'][2] = turn
    if (player_move[0] == 3) and (player_move[1] == 3):
        game_field['row3'][2] = turn
        game_field['col3'][2] = turn
        game_field['diag1'][2] = turn
    return game_field

def check_oncorrect_move(game_field, player_move):
    line = "row" + str(player_move[0])
    if game_field[line][player_move[1] - 1] != '_':
        return False
    else:
        return True

def check_game_status(game_field, turn):
    for line in game_field:
        if (game_field[line].count('0') == 3)  or (game_field[line].count('X') == 3):
            print(game_field['row1'])
            print(game_field['row2'])
            print(game_field['row3'])
            print("Выиграл " + turn)
            return True
    return False

X0X_game()

