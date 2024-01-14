"""Encontrar números primos é uma tarefa difícil. Faça um programa que gera uma lista dos números primos existentes entre 1 e um número inteiro informado pelo usuário"""

n = int(input("enter an integer: "))

primes = [1]

for index in range(2, n + 1):
    is_prime = True

    for num in range(2, int(index ** 0.5) + 1):
        if index % num == 0:
            is_prime = False
            break

    if is_prime:
        primes.append(index)

print(primes)