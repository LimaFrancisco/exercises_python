"""Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos. """

quantity_of_classes = int(input("how many classes: "))

media = 0

for index in range(0, quantity_of_classes):
    media +=  int(input("how many students are in this class? "))

media = media / quantity_of_classes

print(f"\nthe agerage number of students per classes is {media:.0f}")