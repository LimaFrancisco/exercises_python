"""Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores. """

def pair_and_odd(valor):
    if valor % 2 == 0:
        return True
    else:
        return False

num = []
pair = []
odd = []

for index in range(0, 20):

    try:
        num.append(int(input("enter an integer: ")))
    
        if pair_and_odd(num[index]):
            pair.append(num[index])
        else:
            odd.append(num[index])
    except ValueError:
            print("Invalid value")

print(f"\nall values = {num}\npair values = {pair}\nodd values = {odd}")
