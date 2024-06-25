from typing import Type

class Quadrado:

    # costructor
    def __init__(self, tamanho_do_lado: Type[float]) -> Type[None]: 
        self.__tamanho_do_lado = tamanho_do_lado

    # getters and setters
    def get_tamanho_do_lado(self) -> Type[float]:
        return self.__tamanho_do_lado
    
    def set_tamanho_do_lado(self, novo_tamanho: Type[float]) -> Type[None]:
        self.__tamanho_do_lado = novo_tamanho
        
    # another method
    def area_do_quadrado(self) -> Type[float]:
        return self.__tamanho_do_lado ** 2
    