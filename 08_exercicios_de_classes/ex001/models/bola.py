from typing import Type

class Bola:

    # constructor
    def __init__(self, cor: Type[str], circunferencia: Type[float], material: Type[str]) -> Type[None]:
        self.__cor = cor
        self.__circunferencia = circunferencia
        self.__material = material

    # getters and setters
    def get_cor(self) -> Type[str]:
        return self.__cor
    
    def set_cor(self, nova_cor: Type[str]) -> Type[None]:
        self.__cor = nova_cor
        