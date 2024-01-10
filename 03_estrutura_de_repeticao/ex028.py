"""Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um."""

cds = int(input("enter the quantity of cds: "))
amount_invested = 0

for index in range(0, cds):
    amount_invested += float(input("enter the cd value: "))

average_value = amount_invested / cds

print(f"total invested: R$ {amount_invested:.2f}\naverage value per cd: R$ {average_value:.2f}")