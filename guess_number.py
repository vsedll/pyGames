import numpy as np

def game():
    print("Игра называется угадай число, компьютер загадывает число,")
    print("а вам нужно его угадать.")
    
    while True:
        print("Компьютер загадал число...")
        rand_num = np.random.random_integers(100)
        while True: 
            try:                     
                player_guess = int(input("Введите загаданное число: "))
                if player_guess > rand_num:
                    print("Ха ха! Загаданное число меньше!")
                elif player_guess < rand_num:                                
                    print("Ха ха! Загаданное число больше!")
                else:
                    print("Верно! Вы победили, сэр!")
                    break        

            except:
                print("Нужно ввести число!!!")
        
        if input("Для продолжения игры нажмите 'Y' :>").lower() != 'y':
            break
        print("Продолжаем играть!")



if __name__ == "__main__":
    game()
    

