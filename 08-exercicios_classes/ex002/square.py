"""Classe Quadrado: Crie uma classe que modele um quadrado: 
    Atributos: Tamanho do lado
    Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área; 
"""
class square:
    #construtor
    def __init__(self, size_side):
        self.size_side = size_side

    #methods
    def change_size_side(self, new_size_side):
        self.size_side = new_size_side
    
    def show_size_side(self):
        print(self.size_side)

    def area(self):
        print(f"{self.size_side ** 2}")