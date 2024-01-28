"""O cardápio de uma lanchonete é o seguinte:
Especificação   Código  Preço
Cachorro Quente 100     R$ 1,20
Bauru Simples   101     R$ 1,30
Bauru com ovo   102     R$ 1,50
Hambúrguer      103     R$ 1,20
Cheeseburguer   104     R$ 1,30
Refrigerante    105     R$ 1,00
Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido. Considere que o cliente deve informar quando o pedido deve ser encerrado.
"""

menu = {
    100: {'specification': 'Cachorro Quente', 'price': 1.20},
    101: {'specification': 'Bauru Simples', 'price': 1.30},
    102: {'specification': 'Bauru com ovo', 'price': 1.50},
    103: {'specification': 'Hambúrguer', 'price': 1.20},
    104: {'specification': 'Cheeseburguer', 'price': 1.30},
    105: {'specification': 'Refrigerante', 'price': 1.00}
}

order = {}
total = 0

while True:
    code = int(input('Enter the code of the desired item: '))
    if code == 0:
        break
    quantidade = int(input('enter the desired quantity: '))
    if code not in menu:
        print('invalid code.')
    else:
        price = menu[code]['price']
        valor = price * quantidade
        order[code] = {'specification': menu[code]['specification'], 'price': price, 'amount': quantidade, 'valor': valor}
        total += valor

print('\nOrder:')
for code in order:
    item = order[code]
    print(f"{item['specification']} - {item['amount']} x R$ {item['price']} = R$ {item['valor']:.2f}")
print(f'Total: R$ {total:.2f}')
