from typing import Type

class Televisor:

    # constructor
    def __init__(self) -> Type[None]:
        self.__canal = 1
        self.__volume = 35

    # main methods
    def aumentar_volume(self) -> Type[str]:
        if self.__verificar_volume():
            self.__volume = self.__volume + 5
        return 'VOLUME: ' + '|' * self.__volume

    def diminuir_volume(self) -> Type[str]:
        if self.__verificar_volume():
            self.__volume = self.__volume - 5
        return 'VOLUME: ' + '|' * self.__volume

    def avancar_canal(self) -> Type[str]:
        if self.__verificar_canal():
            self.__canal = self.__canal + 1
        return f'CANAL: {self.__canal}'
        
    def voltar_canal(self) -> Type[str]:
        if self.__verificar_canal() and self.__canal - 1 != 0:
            self.__canal = self.__canal - 1
        return f'CANAL: {self.__canal}'

    # another methods
    def __verificar_canal(self) -> Type[bool]:
        if self.__canal >= 1 and self.__canal < 100:
            return True
        else:
            return False

    def __verificar_volume(self) -> Type[bool]:
        if self.__volume >= 0 and self.__volume < 100:
            return True
        else:
            return False
        