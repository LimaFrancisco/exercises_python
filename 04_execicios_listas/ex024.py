"""Faça um programa que simule um lançamento de dados. Lance o dado 100 vezes e armazene os resultados em um vetor . Depois, mostre quantas vezes cada valor foi conseguido. Dica: use um vetor de contadores(1-6) e uma função para gerar numeros aleatórios, simulando os lançamentos dos dados."""

from random import randint

counter = [0] * 6
values = []

for index in range(0,100):
    values.append(randint(1,6))

    counter[values[index] - 1] += 1

print("number of times each value was achieved:")
for index in range(0, 6):
    print(f"{index + 1} - {counter[index]} times")