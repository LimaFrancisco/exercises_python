from typing import Type

class Ponto:

    # constructor
    def __init__(self, eixo_x: Type[float], eixo_y: Type[float]) -> Type[None]:
        self.__eixo_x = eixo_x 
        self.__eixo_y = eixo_y

    # methods
    def get_x(self) -> Type[float]:
        return self.__eixo_x
    
    def get_y(self) -> Type[float]:
        return self.__eixo_y
