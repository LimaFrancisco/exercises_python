"""Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido. """

num = int(input("insert a value correspondig to the dday of the week(1-sunday, 2-monday...) "))

if num == 1:
    print("sunday")
elif num == 2:
    print("monday")
elif num == 3:
    print("tuesday")
elif num == 4:
    print("wednesday")
elif num == 5:
    print("thursday")
elif num == 6:
    print("friday")
elif num == 7:
    print("saturday")
else:
    print("invalid value")