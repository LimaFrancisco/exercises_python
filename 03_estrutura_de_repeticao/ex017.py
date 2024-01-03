"""Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120 """

n = int(input("enter a number: "))

result = 1 

for index in range(1, n + 1):
    result *= index

print(f"fat of {n} = {result}")