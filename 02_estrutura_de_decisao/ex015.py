"""Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.

    Dicas:
    Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
    Triângulo Equilátero: três lados iguais;
    Triângulo Isósceles: quaisquer dois lados iguais;
    Triângulo Escaleno: três lados diferentes;"""

print("give a three size of a triangle: ")
size1 = float(input())
size2 = float(input())
size3 = float(input())

if size1 < (size2 + size3) and size2 < (size1 + size3) and size3 < (size1 + size3):

        if size1 == size2 and size2 == size3:
            print("equilateral triangle")
        elif size1 == size2 or size1 == size3 or size2 == size3:
            print("isosceles trangle")
        else:
             print("scalene triangle")
else:
    print("values cannot be sides of a triangle")