import numpy as np



def Gibbet_game():
    print("В этой игре от вас требуется угадать загаданное слово.")
    print("Вы угадываете по буквам, если в загаданном слове таких букв нет вы потеряете 1 жизнь!")
    print("У вас есть пять попыток...")    
    lifes = 5

    set_Of_Words = ["Слово","Сковорода",'Работа',"Ноутбук","Лямбда","Парсер"]
    while True:
        print("Игра началась! Выбираем слово...")
        np.random.shuffle(set_Of_Words)
        ask_word = set_Of_Words.pop()
        word_state = list("-" * len(ask_word))
        print("-" * len(ask_word))
        while (lifes > 0) and (check_game_state(word_state)):
            letter = input("Введите букву: ")
            if (ask_word.count(letter) == 0):
                lifes -=1
                print("Такой буквы нет. у вас осталось {0} попыток".format(lifes))
            else:
                i = 0
                for l in ask_word:
                    if (letter == l):
                            word_state[i] = l                            
                    i += 1

            print(word_state)

        if not check_game_state(word_state):
            print("Вы победили, поздравляем!")
        else:
            print("К сожалению вы проиграли...Вы отгадывали слово - {0}".format(ask_word))



def check_game_state(word_state):
    if word_state.count('-') > 0:
        return True
    else:
        return False

Gibbet_game()





        

