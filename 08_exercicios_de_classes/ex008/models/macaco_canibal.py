from models import Macaco
from typing import List, Type

class MacacoCanibal(Macaco):

    # constructor    
    def __init__(self, nome: Type[str]) -> Type[None]:
        super().__init__(nome)
        
    # methods
    def comer(self, macaco: Type[Macaco]) -> Type[None]:
        self._bucho.append(macaco)
    
    def mostrar_bucho(self) -> type[str]:
        retorno = ''
        for item in range(len(self._bucho)):
            retorno = retorno + self._bucho[item]._get_nome() + '\n'
        
        return retorno
    