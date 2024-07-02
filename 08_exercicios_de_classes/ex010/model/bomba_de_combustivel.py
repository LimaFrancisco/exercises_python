from typing import Type

class BombaDeCombustivel:

    # constructor
    def __init__(self, tipo_de_combustivel: Type[str], valor_litro: Type[float], quantidade_combustivel: Type[float]) -> Type[None]:
        self.__tipo_de_combustivel = tipo_de_combustivel
        self.__valor_litro = valor_litro
        self.__quantidade_combustivel = quantidade_combustivel

    # methods
    def abastecer_por_valor(self, valor: Type[float]) -> Type[float]:
        litros = valor / self.__valor_litro
        self.__quantidade_combustivel -= litros
        return litros
    
    def abastecer_por_litro(self, litro: Type[float]) -> Type[float]:
        valor = litro * self.__valor_litro
        self.__quantidade_combustivel -= litro
        return valor
    
    def alterar_valor_combustivel(self, novo_valor: Type[float]) -> Type[None]:
        self.__valor_litro = novo_valor
    
    def alterar_tipo_combustivel(self, novo_tipo: Type[str]) -> Type[None]:
        self.__tipo_de_combustivel = novo_tipo

    def alterar_quantidade_combustivel(self, nova_quantidade: Type[float]) -> Type[None]:
        self.__quantidade_combustivel = nova_quantidade

    def mostrar_dados(self) -> Type[str]:
        dados = f'Tipo de Combustível: {self.__tipo_de_combustivel}\n'
        dados += f'Valor do Combustível por litro: R$ {self.__valor_litro:.2f}\n'
        dados += f'Quantidade de Combustível na bomba: {self.__quantidade_combustivel:.2f}'
        return dados
    