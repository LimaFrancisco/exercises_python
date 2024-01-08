"""Faça um programa que calcule o mostre a média aritmética de N notas. """

num = int(input("number of notes for entry: "))
media = 0

for index in range(1, num + 1):
    media += float(input(f"note #{index}: " ))

media = media / num

print(f"\nmedia of notes: {media:.2f}")