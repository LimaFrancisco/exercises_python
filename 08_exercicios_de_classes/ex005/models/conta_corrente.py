import random
from typing import Type

class ContaCorrente:

    # constructor
    def __init__(self, numero_da_conta: Type[int], correntista_nome: Type[str]) -> Type[None]:
        self.__numero_da_conta = numero_da_conta
        self.__correntista_nome = correntista_nome
        self.__saldo = 0

    # main methods
    def alterar_nome(self, novo_nome: Type[str]) -> None:
        self.__correntista_nome = novo_nome

    def depositar(self, dinheiro: Type[float]) -> Type[str]:
        if self.__chercar_deposito(dinheiro):
            self.__saldo = self.__saldo + dinheiro
            return self.__retornar_deposito_realizado()
        else:
            return self.__retornar_deposito_invalido()

    def sacar(self, dinheiro: Type[float]):
        if self.__checar_saque(dinheiro):
            self.__saldo = self.__saldo - dinheiro

    def mostrar_dados(self) -> Type[str]:
        return f'Nome: {self.__correntista_nome}\nNúmero da conta: {self.__numero_da_conta}\nSaldo: R$ {self.__saldo:.2f}'

    # another methods
    def __checar_saque(self, dinheiro) -> Type[bool]:
        if dinheiro <= self.__saldo :
            return True
        else:
            return False

    def __chercar_deposito(self, dinheiro) -> Type[bool]:
        if dinheiro > 0:
            return True
        else:
            return False
    
    def __retornar_deposito_realizado(self) -> Type[str]:
        return 'Deposito realizado com sucesso'

    def __retornar_deposito_invalido(self) -> Type[str]:
        return 'Deposito invalido'
    