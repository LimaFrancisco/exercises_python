"""Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:

    Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
    Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
    Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
    Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário; """

import math

print("enter three values for the equation: ")

a = float(input())

if a != 0:
    b = float(input())
    c = float(input())

    delta = (b ** 2) - (4 * a * c)

    if delta < 0:
        print("the equation has no real roots")

    elif delta == 0:
        bhaskara = -b / (2 * a)

        print(f"delta equal to zero\nroot: {bhaskara:.2f}")
    
    elif delta > 0:
        root1 = (-b + math.sqrt(delta)) / (2 * a)
        root2 = (-b - math.sqrt(delta)) / (2 * a)

        print(f"the roots of the equation are {root1:.2f} and {root2:.2f}")
else:
    print("a quadratic equation cannot be created because \"a\" is equal to zero")