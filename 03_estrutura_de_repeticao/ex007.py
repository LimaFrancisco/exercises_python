"""Faça um programa que leia 5 números e informe o maior número."""

numbers = []
higher = 0

for index in range(5):
    number = int(input("enter a number: "))
    numbers.append(number)

    if number > higher:
        higher = number

print(f"\nthe higher number is {higher}")