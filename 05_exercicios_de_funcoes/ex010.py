"""Jogo de Craps. Faça um programa de implemente um jogo de Craps. O jogador lança um par de dados, obtendo um valor entre 2 e 12. Se, na primeira jogada, você tirar 7 ou 11, você um "natural" e ganhou. Se você tirar 2, 3 ou 12 na primeira jogada, isto é chamado de "craps" e você perdeu. Se, na primeira jogada, você fez um 4, 5, 6, 8, 9 ou 10,este é seu "Ponto". Seu objetivo agora é continuar jogando os dados até tirar este número novamente. Você perde, no entanto, se tirar um 7 antes de tirar este Ponto novamente. """

from random import randint
from os import system

def menu():

    print(f"{"-" * 21}\n   The Crap Game\n{"-" * 21}")
    input("\npress enter to roll the dice...  ")
    system('cls')


def firstPlay(point):

    if point in [7,11]:
        return "Natural, You Win!"
    elif point in [2,3,12]:
        return "Crap, You Lose!"
    else:
        return "The Game Continues...\n"


def pointMode(point):

    while True:
        print(f"{"-" * 14}\n  Point Mode\n{"-" * 14}\n")
        input("press enter for roll dices...")
        system('cls')

        play = randint(2,12)
        print(f"you got {play} when rolling the dice")

        if play == point:
            return "\nYou Win The Game!"
        elif play == 7:
            return "\nYou Lose!"
        else:
            print("\nPlay again!")


menu()

point = randint(2,12)

print(f"you got {point} when rolling the dice")

first = firstPlay(point)
print(first)

if first == "The Game Continues...\n":
    point = pointMode(point)
    print(point)