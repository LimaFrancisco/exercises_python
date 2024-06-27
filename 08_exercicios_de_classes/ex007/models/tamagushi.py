from typing import Type

class Tamagushi:

    # constructor
	def __init__(self, nome: Type[str], idade: Type[int]) -> Type[None]:
		self.__nome = nome
		self.__idade = idade
		self.__fome = 100
		self.__saude = 100

    # getters and setters
	def get_nome(self) -> Type[str]:
		return self.__nome

	def set_nome(self, novo_nome: Type[str]) -> Type[None]:
		self.__nome = novo_nome

	def get_idade(self) -> Type[int]:
		return self.__idade

	def set_idade(self, nova_idade: Type[int]) -> Type[None]:
		self.__idade = nova_idade

	def get_fome(self) -> Type[int]:
		return self.__fome

	def set_fome(self, nova_fome: Type[int]) -> Type[None]:
		self.__fome = nova_fome

	def get_saude(self) -> Type[int]:
		return self.__saude

	def set_saude(self, nova_saude: Type[int]) -> Type[None]:
		self.__saude = nova_saude

	def get_humor(self) -> Type[str ]:
		if self.get_fome() >= 70 and self.get_saude() >= 70:
			return "Eu estou feliz!"

		elif self.get_fome() >= 50 and self.get_saude() >= 50:
			return "Eu não me sinto muito bem!"

		elif self.get_fome() >= 30 and self.get_saude() >= 30:
			return "Eu tenho muita fome!"

		else:
			return "Estou tão fraco que não consigo responder!"
