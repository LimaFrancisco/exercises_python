"""Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário. O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos. Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados. """

n = int(input("enter an integer: "))

primes = []
divisions = 0
for index in range(2, n+1):
    is_prime = True
    for num in range(2, int(index ** 0.5) + 1):
        divisions += 1
        if index % num == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(index)


print(f'primes: {primes}')
print(f'divisions performed: {divisions}')