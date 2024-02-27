"""
Jogo de Forca. Desenvolva um jogo da forca. O programa terá uma lista de palavras lidas de um arquivo texto e escolherá uma aleatoriamente. O jogador poderá errar 6 vezes antes de ser enforcado
Digite uma letra: A
-> Você errou pela 1ª vez. Tente de novo!

Digite uma letra: O
A palavra é: _ _ _ _ O

Digite uma letra: E
A palavra é: _ E _ _ O

Digite uma letra: S
-> Você errou pela 2ª vez. Tente de novo!
"""
from random import randint
from os import system

errors = 0
correct = 0

file = open('ex011/words.txt','r')
words = list(file)
file.close()

for item in range(0, len(words)):
    words[item] = words[item].replace('\n', '')

selectedWord = words[randint(0,21)]
hiddenWord = "_ _ _ _ _ _" 

while errors < 6: 
    letter = input("Digite uma letra: ")
    letter.lower()

    if letter in selectedWord:  
        for item in range(0, 6):
            if letter == selectedWord[item]:
                hiddenWord = hiddenWord[:item * 2] + selectedWord[item] + hiddenWord[(item * 2) + 1:]
                correct += 1
        print(hiddenWord)
        if correct == 6:
            system('cls')
            print("You Win!")
            exit()

    else:
        errors += 1
        print(f"You made a mistake for the {errors} time. Try again!")

else:
    system('cls')
    print("You Lose!")
