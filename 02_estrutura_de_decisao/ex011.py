"""As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.

    Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
    salários até R$ 280,00 (incluindo) : aumento de 20%
    salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
    salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
    salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
    o salário antes do reajuste;
    o percentual de aumento aplicado;
    o valor do aumento;
    o novo salário, após o aumento."""

salary = float(input("enter the enployee's salary: "))

if salary <= 280.00:
    print(f"current wage R$ {salary:.2f}\nthe percentage of increase applied 20%\nincrease value R$ {salary * 0.2:.2f}\nthe new salary R${salary + (salary * 0.2):.2f}")

elif salary > 280.00 and salary <= 700.0:
    print(f"current wage R$ {salary:.2f}\nthe percentage of increase applied 15%\nincrease value R$ {salary * 0.15:.2f}\nthe new salary R${salary + (salary * 0.15):.2f}")

elif salary > 700.00 and salary <= 1500.00:
    print(f"current wage R$ {salary:.2f}\nthe percentage of increase applied 10%\nincrease value R$ {salary * 0.1:.2f}\nthe new salary R${salary + (salary * 0.1):.2f}")

elif salary > 1500.00:
    print(f"current wage R$ {salary:.2f}\nthe percentage of increase applied 5%\nincrease value R$ {salary * 0.05:.2f}\nthe new salary R${salary + (salary * 0.05):.2f}")
