from typing import Type

class Retangulo:

    # constructor
    def __init__(self, base: Type[float], altura: Type[float]) -> Type[None]:
        self.__base = base
        self.__altura = altura

    # getters and setters
    def get_base(self) -> Type[float]:
        return self.__base

    def set_base(self, nova_base: Type[float]) -> Type[None]:
        self.__base = nova_base

    def get_altura(self) -> Type[float]:
        return self.__altura
    
    def set_altura(self, nova_altura: Type[float]) -> Type[None]:
        self.__altura = nova_altura

    # another_method
    def calcular_area(self) -> Type[float]:
        return self.__base * self.__altura
    
    def calcular_perimetro(self) -> Type[float]:
        return 2 * (self.__base + self.__altura)
    