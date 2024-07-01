from typing import Type
from .ponto import Ponto

class Retangulo:

    # constructor
    def __init__(self, base: Type[float], altura: Type[float]) -> Type[None]:
        self.__base = base
        self.__altura = altura

    # getters and setters
    def get_base(self) -> Type[float]:
        return self.__base
    
    def get_altura(self) -> Type[float]:
        return self.__altura

    def get_centro(self) -> Type[Ponto]:
        return self.__centro

    def get_vertice(self) -> Type[Ponto]:
        return self.__vertice_inferior_esquerdo
    
    def set_altura(self, nova_altura: Type[float]) -> Type[None]:
        self.__altura = nova_altura
    
    def set_base(self, nova_base: Type[float]) -> Type[None]:
        self.__base = nova_base

    # another methods
    def calcular_vertice_inferior_esquerdo(self) -> Type[Ponto]:
        metade_base = self.__base / 2
        metade_altura = self.__altura / 2

        x = self.__centro.get_x() - metade_base
        y = self.__centro.get_y() - metade_altura
        
        vertice = Ponto(x, y)

        return vertice

    def obter_centro(self) -> Type[Ponto]:
        x = self.__base / 2
        y = self.__altura / 2
        centro = Ponto(x, y)
        return centro 
    