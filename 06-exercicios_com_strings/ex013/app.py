"""Jogo da palavra embaralhada. Desenvolva um jogo em que o usuário tenha que adivinhar uma palavra que será mostrada com as letras embaralhadas. O programa terá uma lista de palavras lidas de um arquivo texto e escolherá uma aleatoriamente. O jogador terá seis tentativas para adivinhar a palavra. Ao final a palavra deve ser mostrada na tela, informando se o usuário ganhou ou perdeu o jogo"""

from random import shuffle
from random import randint

file = open("ex013/words.txt","r")

wordList = list(file)

file.close()
answer = ""
attempts = 6

for index in range(0, len(wordList)):
    wordList[index] = wordList[index].replace("\n","")

randomWord = wordList[randint(0,len(wordList))]

scrambled_word = list(randomWord)
shuffle(scrambled_word)
scrambled_word = "".join(scrambled_word)

while True:
    answer = input(f"guess the word \"{scrambled_word}\": ")
    answer.lower()
    answer.split()

    if answer == randomWord:
        print(f"You Win! The secret word is \"{randomWord}\"")
        break
    elif attempts == 1:
        print(f"You Lose! The secret word is \"{randomWord}\"")
        break
    else:
        print("Wrong word! Try again!")

    attempts = attempts - 1

    print(f"number of attempts: {attempts}\n")