"""Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada. """

num = int(input("enter a number of people: "))

media = 0

for index in range(0, num):
    media += int(input("informe a age: "))

media = media / num



print(f"the media of age class is {media:.0f}")

if media > 0  and media <= 25:
    print("young class")
elif media >= 26  and media <= 60:
    print("adult class")
elif media > 60:
    print("senior class")