"""Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.

    Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
    comprar apenas latas de 18 litros;
    comprar apenas galões de 3,6 litros;
    misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias. """

import math

size = float(input("enter the size of the wall in square meters: "))

liters = (size * 1.1) / 6 # 10%

print(f"do you need {liters:.2f} liters of paint")
print("\ndo you can buy in three forms:")

#can

if liters < 18:
    print("1 - 1 can of paint for R$ 80.00")
elif liters % 18 == 0:
    print(f"1 - {liters / 18:.2f} cans of paint for R$ {(liters / 18) * 80.00:.2f}")
elif liters % 18 > 0:
    print(f"1 - {(liters // 18) + 1:.2f} cans of paint for R$ {((liters // 18) + 1) * 80.00:.2f}")

#galon

if liters < 3.6:
    print("2 - 1 can of paint for R$ 25.00")
elif liters % 3.6 == 0:
    print(f"2 - {liters / 3.6:.2f} cans of paint for R$ {(liters / 3.6) * 25.00:.2f}")
elif liters % 3.6 > 0:
    print(f"2 - {(liters // 3.6) + 1:.2f} cans of paint for R$ {((liters // 3.6) + 1) * 25.00:.2f}")

# can and galon

if liters < 3.6:
    print("3 - 1 galon of paint for R$ 25.00")
elif (liters >= 3.6) and (liters < 18):
    if liters % 3.6 == 0:
        print(f"3 - {liters / 3.6:.2f} galon(s) of paint for R${(liters / 3.6) * 25.00:.2f}")
    elif liters % 3.6 != 0:
        print(f"3 - {(liters / 3.6) + 1:.2f} galon(s) of paint for R${((liters / 3.6) + 1) * 25.00:.2f}")
elif liters % 18 == 0:
    print(f"3 - {liters / 18:.2f} cans of paint for R$ {(liters / 18) * 80.00:.2f}")
elif (liters % 18) % 3.6 > 0:

    can = liters // 18
    galon = 0

    if (liters % 18) % 3.6 == 0:
        galon = (liters % 18) / 3.6
    else:
        galon = math.ceil((liters % 18) / 3.6)

    print(f"3 - {can:.0f} can(s) of paint and {galon:.0f} galon(s) for R$ {(can * 80.00) + (galon * 25.00):.2f}")