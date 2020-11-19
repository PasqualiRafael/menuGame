from modules import show_title
from modules.colors import cores
from random import randint
from time import sleep
import os


def jogar():

    show_title.ini(' Adivinhe o numero ')
    max_num = randint(100, 1000)
    pc_num = randint(0, max_num)
    global user_round
    user_round = 1
    global num_try
    num_try = 0
    my_numbers = list()

    def difficulty():
        global num_try
        print(f'Escolha a dificuldade:')
        dificuldade = str(input(f'(1) Facil | (2) Normal | (3) Dificil\n'))
        while dificuldade not in '123':
            dificuldade = str(input(f'(1) Facil | (2) Normal | (3) Dificil\n'))
            if dificuldade not in '123':
                print(f'Essa opcao nao existe.\n')
        if dificuldade == '1':
            num_try = 30
        elif dificuldade == '2':
            num_try = 20
        elif dificuldade == '3':
            num_try = 10
        choose()

    def score():
        _score = 30000 - (pc_num * user_round)
        return _score

    def clear_screen(x):
        os.system('clear')
        adv(x)

    def choose():
        print(f'Rodada {user_round} de {num_try}.')
        user_choose = int(input(f'Escolha um numero entre 0 e {max_num}.\n'))
        my_numbers.append(user_choose)
        sleep(0.5)
        clear_screen(user_choose)

    def adv(num):
        global user_round
        show_title.ini(' Adivinhe o numero ')
        if pc_num == num:
            print(f'Parabens voce adivinhou')
            print(f'Score: {score()}')
            print(f'Pc: {pc_num}\nYou: {my_numbers}')
        else:
            user_round += 1
            if user_round > num_try:
                print(f'Voce perdeu.')
            while pc_num != num and user_round <= num_try:
                if num > pc_num:
                    print(f'Tente novamente, o numero é {cores["red"]}menor.{cores["close"]}')
                    print(f'Numero anterior: {cores["green"]}{num}{cores["close"]}\n')
                    break
                else:
                    print(f'Tente novamente, o numero é {cores["red"]}maior.{cores["close"]}')
                    print(f'Numero anterior: {cores["green"]}{num}{cores["close"]}\n')
                    break

            choose()
    difficulty()
    show_title.close()


if __name__ == '__main__':
    jogar()


