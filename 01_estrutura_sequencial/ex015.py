"""Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$"""

salary_hour = float(input("enter your hourly salary: "))
total_hours = float(input("report the total hours worked: "))

gross_salary = salary_hour * total_hours
ir = gross_salary * 0.11
inss = gross_salary * 0.08
sydicate = gross_salary * 0.05
net_salary = gross_salary - (ir + inss + sydicate)

print(f"gross salary R$ {gross_salary:.2f}")
print(f"ir R$ {ir:.2f}")
print(f"inss R$ {inss:.2f}")
print(f"syndicate R$ {sydicate:.2f}")
print(f"net salary R$ {net_salary:.2f}")