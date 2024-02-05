"""Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0. """

best = 0
notes = []

for index in range(0, 10):
    notes = []
    average = 0

    try:
        for note in range(0, 4):
            notes.append(float(input(f"enter student {index+1:.0f}'s grades: ")))
            average += notes[note]

        average = average / 4 

        if average >= 7:
            best += 1
    
    except ValueError:
            print("Invalid value")

    print("\n")

print(f"{best:.0f} students managed to obtain an average greater than or equal to 7.0")