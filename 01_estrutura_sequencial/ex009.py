# Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
fehrenheit = float(input())

celsius = 5 * ((fehrenheit - 32) / 9)

print(f"{fehrenheit:.4f} fehrenheit it's equivalent to {celsius:.4f} celsius")