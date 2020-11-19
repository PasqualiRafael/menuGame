from random import choice
from time import sleep
from modules import show_title
from modules.colors import cores


def jogar():
    show_title.ini(' Jokenpô ')

    # input
    user_choose = str(input('Escolha papel, pedra ou tesoura:\n')).lower().strip()

    # var
    cpu_list = ['papel', 'pedra', 'tesoura']
    cpu_choose = choice(cpu_list)

    # sleep
    print('{}3{}\n'.format(cores['bw'], cores['close']))
    sleep(1)
    print('{}2{}\n'.format(cores['bw'], cores['close']))
    sleep(1)
    print('{}1{}\n'.format(cores['bw'], cores['close']))
    sleep(1)

    # condition
    if user_choose == 'papel' or user_choose == 'pedra' or user_choose == 'tesoura':
        if user_choose == 'papel' and cpu_choose == 'pedra':
            print('O computador escolheu: {}{}{}'.format(cores['purple'], cpu_choose, cores['close']))
            print('{}Parabéns, voce Venceu{}'.format(cores['green'], cores['close']))
        elif user_choose == 'pedra' and cpu_choose == 'tesoura':
            print('O computador escolheu: {}{}{}'.format(cores['purple'], cpu_choose, cores['close']))
            print('{}Parabéns, voce Venceu{}'.format(cores['green'], cores['close']))
        elif user_choose == 'tesoura' and cpu_choose == 'papel':
            print('O computador escolheu: {}{}{}'.format(cores['purple'], cpu_choose, cores['close']))
            print('{}Parabéns, voce Venceu{}'.format(cores['green'], cores['close']))
        elif user_choose == cpu_choose:
            print('O computador escolheu: {}{}{}'.format(cores['purple'], cpu_choose, cores['close']))
            print('{}O jogo Empatou{}'.format(cores['grey'], cores['close']))
        else:
            print('O computador escolheu: {}{}{}'.format(cores['purple'], cpu_choose, cores['close']))
            print('{}Tente de novo, você Perdeu{}'.format(cores['red'], cores['close']))
    else:
        print('Voce precisa digitar uma das opções')

    show_title.close()


if __name__ == "__main__":
    jogar()
