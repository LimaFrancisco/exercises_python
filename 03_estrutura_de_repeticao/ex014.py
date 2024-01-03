"""Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares. """

numbers = []

pair = 0
odd = 0

for index in range(0, 10):
    number = int(input("enter a number: "))
    numbers.append(number)

    if number % 2 == 0:
        pair += 1
    else:
        odd += 1

print(f"quantity of pair numbers = {pair}")
print(f"quantity of odd numbers = {odd}")