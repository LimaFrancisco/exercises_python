from typing import Type

class Pessoa:

    def __init__(self, nome: Type[str]) -> Type[None]:
        self.__nome = nome
        self.__idade = 0
        self.__peso = 4.1
        self.__altura = 0.55

    def get_nome(self) -> Type[str]:
        return self.__nome
    
    def get_idade(self) -> Type[int]:
        return self.__idade
    
    def get_peso(self) -> Type[float]:
        return self.__peso
    
    def get_altura(self) -> Type[float]:
        return self.__altura

    def envelhecer(self) -> Type[None]:
        self.__idade = self.__idade + 1 
        if self.__idade < 21:
            self.__altura = self.__altura + 0.005

    def engordar(self) -> Type[None]:
        self.__peso = self.__peso + 1

    def emagrecer(self) -> Type[None]:
        self.__peso = self.__peso - 1

    def crescer(self) -> Type[None]:
        if self.__idade == 1:
            self.__altura = self.__altura + 0.25
        elif 1 < self.__idade < 3:
            self.__altura = self.__altura + 0.125
        elif 3 < self.__idade < 14:
            self.__altura = self.__altura + 0.06
        elif 14 < self.__idade < 21:
            self.__altura = self.__altura + 0.06
    