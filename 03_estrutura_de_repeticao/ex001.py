"""Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido. """

grade = 1

while grade > 0 and grade <=10:
    grade = float(input("informe a note: "))

print("invalid grade")