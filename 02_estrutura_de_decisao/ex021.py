"""Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.

    Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
    Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1. """

to_withdraw = float(input("Enter the amount you want to withdraw: "))
rest = 0

if to_withdraw <= 600 and to_withdraw >= 10:
    
    print(f"to withdraw amounts of {to_withdraw:.2f}")

    if to_withdraw >= 100:
        print(f"the program offers {to_withdraw // 100:.0f} grades out of R$ 100")
        rest = to_withdraw % 100

    if rest >= 50:
        print(f"the program offers {rest // 50:.0f} grades out of R$ 50")
        rest = rest % 50
    
    if rest >= 10:
        print(f"the program offers {rest // 10:.0f} grades out of R$ 10")
        rest = rest % 10
    
    if rest >= 5:
        print(f"the program offers {rest // 5:.0f} grades out of R$ 5")
        rest = rest % 5
    
    if rest < 5 and rest > 0:
        print(f"the program offers {rest:.0f} grades out of R$ 1")
        rest = rest % 100
else:
    print("invalid value")