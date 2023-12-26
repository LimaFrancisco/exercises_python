"""Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.

    Desconto do IR:
    Salário Bruto até 900 (inclusive) - isento
    Salário Bruto até 1500 (inclusive) - desconto de 5%
    Salário Bruto até 2500 (inclusive) - desconto de 10%
    Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220. """
 
hourly_rate = float(input("enter the hourly rate: "))
worked_hours = float(input("report hours worked: "))

gross_salary = hourly_rate * worked_hours

print(f"\nGross Salary: ({hourly_rate:.0f} * {worked_hours:.0f})         : R$ {gross_salary:.2f} ")

#IR

ir = 0

if gross_salary > 900 and gross_salary <= 1500:
    ir = gross_salary * 0.05
    print(f"(-) IR (5%)                     : R$ {ir:.2f}")
elif gross_salary > 1500 and gross_salary <= 2500:
    ir = gross_salary * 0.1
    print(f"(-) IR (10%)                     : R$ {ir:.2f}")
elif gross_salary > 2500:
    ir = gross_salary * 0.2
    print(f"(-) IR (20%)                     : R$ {ir:.2f}")

#INSS

inss = gross_salary * 0.1
print(f"INSS (10%)                      : R$ {inss:.2f}")

#FGTS

fgts = gross_salary * 0.11
print(f"FGTS (11%)                      : R$ {fgts:.2f}")

#TOTAL DISCOUNTS

total = ir + inss
print(f"Total Discounts                 : R$ {total:.2f}")

#NET SALARY
print(f"Net Salary                      : R$ {gross_salary - total:.2f}")