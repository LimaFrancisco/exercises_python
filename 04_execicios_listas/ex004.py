"""Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes"""

def is_consonant(letter):
    letter = letter.lower()
    if letter in 'bcdfghjklmnpqrstvxyz':
        return True
    else:
        return False
    
vector = []
consonant = []

for item in range(0, 10):
    vector.append(input("enter a character: "))

    if is_consonant(vector[item]):
        consonant.append(vector[item])

print(f"\n{consonant}")