"""Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.

    Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
    326 = 3 centenas, 2 dezenas e 6 unidades
    12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16 """

num = int(input("enter an integer less than 1000: "))

hundred = num // 100
tens = (num % 100) // 10
unit = (num % 100) % 10

if num < 1000 and num >= 100:
    print(f"{num} = {hundred} hundred(s), {tens} ten(s), {unit} unit(s)")
elif num <= 99 and num >= 10:
    print(f"{num} = {tens} ten(s), {unit} unit(s)")
elif num <= 9 and num >= 0:
    print(f"{num} = {unit} unit(s)")