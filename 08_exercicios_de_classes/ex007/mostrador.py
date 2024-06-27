from typing import Type
from models import Tamagushi

class Mostrador:

    def exibir_tudo(self, tamagushi: Type[Tamagushi]) -> Type[str]:
        todos_dados = '*' * 5 + ' Dado do meu bichinho virtual ' + '*' * 5 + '\n'
        todos_dados = todos_dados + 'NOME: '+ tamagushi.get_nome() + '\n'
        todos_dados = todos_dados + 'IDADE: ' + str(tamagushi.get_idade()) + '\n'
        todos_dados = todos_dados + 'FOME: ' + str(tamagushi.get_fome()) + '\n'
        todos_dados = todos_dados + 'SAUDE: ' + str(tamagushi.get_saude()) + '\n'
        todos_dados = todos_dados + 'HUMOR: ' + tamagushi.get_humor() + '\n'

        return todos_dados
    