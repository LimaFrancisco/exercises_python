"""Faça um Programa que peça dois números e imprima o maior deles. """

num1 = int(input("enter a number: "))
num2 = int(input("enter other number: "))

if num1 > num2:
    print(f"{num1} is the biggest")
elif num2 > num1:
    print(f"{num2} is the biggest")