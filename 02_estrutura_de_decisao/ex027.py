"""Uma fruteira está vendendo frutas com a seguinte tabela de preços: 

                      Até 5 Kg           Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg

Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente
"""

strawberry = float(input("Enter the number of kilos of strawberries you wish to purchase: "))
apple = float(input("Enter the number of apples of strawberries you wish to purchase: "))

total = 0

if strawberry <= 5:
    total = total + (strawberry * 2.5)
elif strawberry > 5:
    total = total + (strawberry * 2.2)

if apple <= 5:
    total = total + (apple * 1.8)
elif apple > 5:
    total = total + (apple * 1.5)

if (strawberry + apple) > 8 or total > 25:
    total = total - (total * 0.1)
    print(f"you will pay R$ {total:.2f}")
else:
    print(f"you will pay R$ {total:.2f}")