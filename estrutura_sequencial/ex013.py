""" Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
    a - Para homens: (72.7*h) - 58
    b - Para mulheres: (62.1*h) - 44.7 """

height = float(input("what is your height? "))

male = (72.7 * height) - 58
female = (62.1 * height) - 44.7

print(f"ideal weight for men {male:.2f}\nideal weight for women {female:.2f}")