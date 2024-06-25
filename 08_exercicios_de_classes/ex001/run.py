# importando a classe bola
from models import Bola

# criando um objeto bola(instancia da classe Bola)
bola = Bola("Branca", 70, "Couro")
# usando o metodo get_cor() para visualizar o atributo cor
print(bola.get_cor())

# alterando o valor do atributo cor com o metodo set_cor()
bola.set_cor("Preta")
print(bola.get_cor())
