"""Faça um programa que leia 5 números e informe a soma e a média dos números"""

list = []
media = 0

for index in range(5):
    media += int(input("informe a number: ")) 

media = media / 5

print(f"media = {media}")