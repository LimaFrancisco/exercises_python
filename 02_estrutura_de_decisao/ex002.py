"""Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo."""

valor = int(input("enter a integer number: "))

if valor >= 0:
    print(f"{valor} is a positive number")
else:
    print(f"{valor} is a negative number")