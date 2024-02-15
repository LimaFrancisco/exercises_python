"""Faça um programa para imprimir:

        1
        1   2
        1   2   3
        .....
        1   2   3   ...  n

    para um n informado pelo usuário. Use uma função que receba um valor n inteiro imprima até a n-ésima linha."""

def pyramid (n):
    list = [""] * n
    for index in range(0, n):

        count = 1
        while count <= index + 1:
            list[index] += (f"{count} ")
            count += 1
            
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