"""Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno e o segundo representando a sua altura em centímetros. Encontre o aluno mais alto e o mais baixo. Mostre o número do aluno mais alto e o número do aluno mais baixo, junto com suas alturas. """

students = [0] * 10
size = [0] * 10

higher = 0
lower = 0

for index in range(0, 10):
    students[index] = (float(input("enter a number for a student: ")))
    size[index] = (float(input("now insert the student size: ")))

    if size[index] > size[higher]: 
        higher = index
    
    if size[lower] == 0 or size[index] < lower:
        lower = index

print(f"\nhigher student\nstudent number: {students[higher]:.0f}\nsize: {size[higher]:.2f}")
print(f"\nlower student\nstudent number: {students[lower]:.0f}\nsize: {size[lower]:.2f}")