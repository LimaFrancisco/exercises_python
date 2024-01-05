"""Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1. """

num = int(input("enter a integer: "))

if num <= 1:
    print("is not a prime number")

else:
    while not(num % 2 == 0 or num % 3 == 0 or num % 5 == 0 or num % 7 == 0) or (num == 2 or num == 3 or num == 5 or num == 7):
        print("is a prime number")
        break

    else:
        print("is not a prime number")

