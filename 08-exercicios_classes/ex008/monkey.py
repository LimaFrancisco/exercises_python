"""Classe Macaco: Desenvolva uma classe Macaco,que possua os atributos nome e bucho (estomago) e pelo menos os métodos comer(), verBucho() e digerir(). Faça um programa ou teste interativamente, criando pelo menos dois macacos, alimentando-os com pelo menos 3 alimentos diferentes e verificando o conteúdo do estomago a cada refeição. Experimente fazer com que um macaco coma o outro. É possível criar um macaco canibal? """

class Monkey:
    def __init__(self, name):
        self.name = name
        self.stomach = []

    def to_eat(self, food):
        if len(self.stomach) == 3:
            print("full stomach")
            return

        self.stomach.append(food)

    def getStomach(self):
        print(f"{self.name}`s stomach:")
        for food in self.stomach:
            print(food)

    def digest(self):
        self.stomach.clear()
        