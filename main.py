from modules import show_title
import os
import adivinha
import jokenpo
import forca


def menu():

    print(f"Choose your game: ")
    choose_game = "0"
    while choose_game not in "123":
        choose_game = str(input(f"(1) Guess | (2) Jokenpo | (3) Forca.\n"))
        if choose_game not in "123":
            print(f"Essa opcao nao existe.\n")

    if choose_game == "1":
        os.system("clear")
        adivinha.jogar()
    elif choose_game == "2":
        os.system("clear")
        jokenpo.jogar()
    elif choose_game == "3":
        os.system("clear")
        forca.jogar()


if __name__ == "__main__":
    menu()
