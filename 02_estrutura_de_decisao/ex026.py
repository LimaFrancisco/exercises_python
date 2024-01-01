"""Um posto está vendendo combustíveis com a seguinte tabela de descontos:

    Álcool:
    até 20 litros, desconto de 3% por litro
    acima de 20 litros, desconto de 5% por litro
    Gasolina:
    até 20 litros, desconto de 4% por litro
    acima de 20 litros, desconto de 6% por litro Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90"""

response = input("enter the price for the fuel you want?\nA alcohol\nG gasoline\n")
response.lower()
liters = 0

if response == "a":
    liters = float(input("how many liters do you want? "))

    if liters <= 20:
        print(f"{liters:.2f} by R$ {(liters * 1.9) - ((liters * 1.9) * 0.03)}")
    elif liters > 20:
        print(f"{liters:.2f} liters, valor to pay R$ {(liters * 1.9) - ((liters * 1.9) * 0.05)}")

elif response == "g":
    liters = float(input("how many liters do you want? "))

    if liters <= 20:
        print(f"{liters:.2f} by R$ {(liters * 2.5) - ((liters * 2.5) * 0.04)}")
    elif liters > 20:
        print(f"{liters:.2f} liters, valor to pay R$ {(liters * 2.5) - ((liters * 2.5) * 0.06)}")