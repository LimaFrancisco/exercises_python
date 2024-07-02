from model import BombaDeCombustivel

bomba = BombaDeCombustivel('Etanol', 4.83, 10000)

print(bomba.mostrar_dados())

bomba.abastecer_por_litro(15)
bomba.abastecer_por_valor(200)

bomba.alterar_valor_combustivel(6.25)
bomba.alterar_tipo_combustivel('Gasolina')

print('*' * 50)
print(bomba.mostrar_dados())
