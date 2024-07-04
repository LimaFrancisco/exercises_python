from typing import Type

class Carro:

    def __init__(self, consumo: Type[float]) -> Type[None]:
        self.__consumo = consumo
        self.__combustivel_em_tanque = 0

    def andar(self, distancia: Type[float]) -> Type[None]:
        self.__combustivel_em_tanque -= self.__consumo / distancia

    def obter_gasolina(self) -> Type[float]:
        return self.__combustivel_em_tanque
    
    def adicionar_gasolina(self, gasolina: Type[float]) -> Type[None]:
        self.__combustivel_em_tanque += gasolina
