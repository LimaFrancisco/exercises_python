"""Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa."""

vector = []

for index in range(0, 10):
    vector.append(int(input("enter an integer: ")))

vector.reverse()

print(vector)