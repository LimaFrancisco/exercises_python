"""O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira: 

                      Até 5 Kg           Acima de 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg

Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar. 
"""

type_meat = input("which meat do you want?\nF double file\nA rump\nP rump steak\n")
type_meat.lower()

kilo = float(input("how many kilos do you want? "))

card = input("do you have a tabajara card(s/n)? ")
card.lower()

discount = 0

print("description           amount   unity   vl.unit    discount  lv.total")

if type_meat == "f":
    if kilo <= 5:

        if card == "s":
            discount = (kilo * 4.90) * 0.05

        print(f"double file           {kilo:.3f}    kg      R$ 4,90    R$ {discount:.2f}   R$ {(kilo * 4.90) - discount:.2f}")
    elif kilo > 5:

        if card == "s":
            discount = (kilo * 5.80) * 0.05

        print(f"double file           {kilo:.3f}    kg      R$ 5,80    R$ {discount:.2f}   R$ {(kilo * 5.80) - discount:.2f}")

elif type_meat == "a":
    if kilo <= 5:

        if card == "s":
            discount = (kilo * 5.90) * 0.05

        print(f"rump                  {kilo:.3f}    kg      R$ 5,90    R$ {discount:.2f}   R$ {(kilo * 5.90) - discount:.2f}")
    elif kilo > 5:

        if card == "s":
            discount = (kilo * 6.80) * 0.05

        print(f"rump                  {kilo:.3f}    kg      R$ 6,90    R$ {discount:.2f}   R$ {(kilo * 6.80) - discount:.2f}")

elif type_meat == "p":
    if kilo <= 5:

        if card == "s":
            discount = (kilo * 6.90) * 0.05

        print(f"rump steak           {kilo:.3f}    kg      R$ 6,90    R$ {discount:.2f}   R$ {(kilo * 6.90) - discount:.2f}")
    elif kilo > 5:

        if card == "s":
            discount = (kilo * 7.80) * 0.05

        print(f"rump steak            {kilo:.3f}    kg      R$ 7,80    R$ {discount:.2f}   R$ {(kilo * 7.80) - discount:.2f}")