"""Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores. """

n = int(input("enter a quantity of numbers: "))

list = []

for index in range(0, n):
    num = int(input("inform a number: "))
    list.append(num)

bigger = list[0]
smaller = list[0]

for index in range(0, n):
    if list[index] > bigger:
        bigger = list[index]

    if list[index] < smaller:
        smaller = list[index]

print(f"bigger: {bigger}\nsmaller: {smaller}\nsum: {bigger + smaller}")