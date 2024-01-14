"""Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado pelo usuário, mas a tabuada não deve necessariamente iniciar em 1 e terminar em 10, o valor inicial e final devem ser informados também pelo usuário, conforme exemplo abaixo: 

Montar a tabuada de: 5
Começar por: 4
Terminar em: 7

Vou montar a tabuada de 5 começando em 4 e terminando em 7:
5 X 4 = 20
5 X 5 = 25
5 X 6 = 30
5 X 7 = 35
"""

num = int(input("set up the multiplication table: "))
start = int(input("starts with: "))
end = int(input("end by: "))

if start < end:
    print(f"I will set up the {num:.0f} times table starting with {start:.0f} and ending with {end:.0f}:")
    for index in range(start, end + 1):
        print(f"{num:.0f} X {index:.0f} = {num * index:.0f}")
elif start >= end:
    print("impossible to calculate multiplication tables")