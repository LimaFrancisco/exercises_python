# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
hour_value = float(input("what is the value of working hours: "))
worked_hours = float(input("how many hours worked: "))

print(f"salary = R$ {hour_value * worked_hours:.2f}")