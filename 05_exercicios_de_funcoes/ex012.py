"""Embaralha palavra. Construa uma função que receba uma string como parâmetro e devolva outra string com os carateres embaralhados. Por exemplo: se função receber a palavra python, pode retornar npthyo, ophtyn ou qualquer outra combinação possível, de forma aleatória. Padronize em sua função que todos os caracteres serão devolvidos em caixa alta ou caixa baixa, independentemente de como foram digitados"""
from random import shuffle

def scramble_words(word):

    word = list(word)
    shuffle(word)
    word = "".join(word)

    return word

try:
    word = input("enter any word: ")
except ValueError:
    print("invalid data type")

newWord = scramble_words(word)

print(newWord)
