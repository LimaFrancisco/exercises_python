"""Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de arredondamento. """

num = float(input("enter a number: "))

if num == round(num):
    print("integer")
else:
    print("decimal number")