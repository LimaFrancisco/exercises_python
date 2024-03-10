"""Classe Bichinho Virtual:Crie uma classe que modele um Tamagushi (Bichinho Eletrônico):

    Atributos: Nome, Fome, Saúde e Idade b. Métodos: Alterar Nome, Fome, Saúde e Idade; Retornar Nome, Fome, Saúde e Idade Obs: Existe mais uma informação que devemos levar em consideração, o Humor do nosso tamagushi, este humor é uma combinação entre os atributos Fome e Saúde, ou seja, um campo calculado, então não devemos criar um atributo para armazenar esta informação por que ela pode ser calculada a qualquer momento. 
"""

class tamagushi:
    # constructor
    def __init__(self, name, age = 0):
        self.name = name
        self.hunger = False
        self.health = True
        self.age = age
        self.humor = True

    # modifiers
    def changeName(self, newName):
        self.name = newName

    def changeHunger(self):
        if self.hunger:
            self.hunger = False
            self.humor = False
        else:
            self.hunger = True
            self.humor = True

    def changeHealth(self):
        if self.health:
            self.health = False
            self.humor = False
        else:
            self.health = True
            self.humor = True

    def changeAge(self):
        self.age += 1

    # dials
    def showName(self):
        print(f"name: {self.name}")

    def showHunger(self):
        print(f"hunger: {self.hunger}")    

    def showHealth(self):
        print(f"health: {self.health}")

    def showgeAge(self):
        print(f"age: {self.age}")

    def showHumor(self):
        print(f"humor: {self.humor}")
