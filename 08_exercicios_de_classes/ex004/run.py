from models import Pessoa

pessoa = Pessoa("Arthur")

print(f'Nome: {pessoa.get_nome()}')
print(f'Peso: {pessoa.get_peso()}')
print(f'Altura: {pessoa.get_altura()}')
print(f'Idade: {pessoa.get_idade()}')

pessoa.envelhecer()
pessoa.engordar()
pessoa.crescer()
pessoa.envelhecer()
pessoa.engordar()
pessoa.crescer()
pessoa.envelhecer()
pessoa.engordar()
pessoa.crescer()
pessoa.envelhecer()
pessoa.engordar()
pessoa.crescer()

print(f'Nome: {pessoa.get_nome()}')
print(f'Peso: {pessoa.get_peso()}')
print(f'Altura: {pessoa.get_altura()}')
print(f'Idade: {pessoa.get_idade()}')
