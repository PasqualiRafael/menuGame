from modules import show_title
from modules.colors import cores as c
from random import randint
from time import sleep


def jogar():

    show_title.ini(" Forca ")

    def read_secret_word(file_name="secret_words.txt"):
        word_data = open(file_name, "r")
        list_data = word_data.read().lower().split()
        one_word = list_data[randint(0, (len(list_data) - 1))]
        word_data.close()
        return one_word

    secret_word = read_secret_word()
    victory = False
    die = False
    life = 3
    word = list("_" * len(secret_word))
    print(
        "A palavra tem {}{}{} letras.\n".format(c["red"], len(secret_word), c["close"])
    )

    while not victory and not die:

        def msg_input():
            print("")
            print("Voce tem {}{}{} vidas.".format(c["green"], life, c["close"]))
            _letter = str(input(f"Escolha uma letra.\n").lower().strip())
            return _letter

        def find_letter_word():
            for i, v in enumerate(secret_word):
                sleep(0.2)
                if v != letter:
                    print(f"{word[i]}", end="")
                elif v == letter:
                    print(v, end="")
                    word[i] = letter

        letter = msg_input()
        find_letter_word()
        temp_join = "".join(word)

        if letter not in secret_word:
            life -= 1

        if life == 0:
            print("\nVoce Perdeu!")
            die = True

        if temp_join == secret_word:
            print("\nVoce venceu!")
            victory = True

    show_title.close()


if __name__ == "__main__":
    jogar()
