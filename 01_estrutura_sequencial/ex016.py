"""Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total."""

area = float(input("inform the size of the area to be painted in square meters: "))

if area > 54:
    can = (area // 54) 

    if area % 54 != 0:
        can += 1
    
    print(f"you need {can} cans of paint")
else:
    print("you need 1 can of paint")