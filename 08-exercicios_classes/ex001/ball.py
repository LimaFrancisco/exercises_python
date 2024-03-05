"""Classe Bola: Crie uma classe que modele uma bola:
Atributos: Cor, circunferência, material
Métodos: trocaCor e mostraCor 
"""
class ball:
    def __init__(self, color, circumference, material):
        self.color = color
        self.circumference = circumference
        self.material = material

    def show_color(self):
        print(self.color)

    def change_color(self, new_color):
        self.color = new_color