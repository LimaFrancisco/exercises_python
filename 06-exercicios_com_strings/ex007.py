"""Conta espaços e vogais. Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte
quantos espaços em branco existem na frase.
quantas vezes aparecem as vogais a, e, i, o, u. 
"""

sentence = input("enter any sentence: ")

spaces = 0
vowel = 0

for item in sentence:
    if item in ["a","e","i","o","u"]:
        vowel += 1
    elif item == " ":
        spaces += 1

print(f"the sentence has {spaces} space(s) and {vowel} vowel(s)")