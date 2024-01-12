"""Os números primos possuem várias aplicações dentro da Computação, por exemplo na Criptografia. Um número primo é aquele que é divisível apenas por um e por ele mesmo. Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. """

num = int(input("enter a integer: "))
is_prime = 0

for index in range(1, num + 1):
    if num % index == 0:
        is_prime += 1


if is_prime == 2:
    print(f"{num:.0f} is a prime number")
else:
    print(f"{num:.0f} is not a prime number")