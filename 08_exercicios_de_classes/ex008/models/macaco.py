from typing import Type, List

class Macaco:

    # constructor
    def __init__(self, nome: Type[str]) -> Type[None]:
        self.__nome = nome
        self._bucho = []

    # methods
    def comer(self, alimento: Type[str]) -> Type[None]:
        self._bucho.append(alimento)

    def mostrar_bucho(self) -> Type[List]:
        return self._bucho
    
    def digerir(self) -> Type[None]:
        self._bucho.clear()

    def _get_nome(self) -> Type[str]:
        return self.__nome
        