# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
import math
radius = float(input())

area = math.pi * (radius ** 2)

print(f"{area:.2f}")