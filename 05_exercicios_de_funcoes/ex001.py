"""Faça um programa para imprimir: 

    1
    2   2
    3   3   3
    .....
    n   n   n   n   n   n  ... n

para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima até a n-ésima linha. 
"""

def pyramid (n):
    list = []
    for index in range(0, n):
        list.append(f"{index + 1} " * (index + 1))
    
    return list

n = 0

try:
    n = int(input("enter any integer: "))
except ValueError:
    print("invalid data type")

list = pyramid(n)

print("")
for item in list:
    print(item)