# Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
celsius = float(input())

fehrenheit = 32 + (celsius * (9 / 5))

print(f"{celsius:.4f} celsius it's equivalent to {fehrenheit:.4f} fehrenheit")