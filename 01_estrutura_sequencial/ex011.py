""" Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
        a - o produto do dobro do primeiro com metade do segundo .
        b - a soma do triplo do primeiro com o terceiro.
        c - o terceiro elevado ao cubo """

num1 = int(input("enter an integer: "))
num2 = int(input("enter another interger: "))
num3 = float(input("enter a floating-point number: "))

a = (num1 * 2) * (num2 / 2)
b = (num1 * 3 ) + num3
c = num3 ** 3

print(f"\na = {a:.2f}\nb = {b:.2f}\nc = {c:.2f}")