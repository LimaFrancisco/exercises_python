"""Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça:

Mostre a quantidade de valores que foram lidos;
Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
Calcule e mostre a soma dos valores;
Calcule e mostre a média dos valores;
Calcule e mostre a quantidade de valores acima da média calculada;
Calcule e mostre a quantidade de valores abaixo de sete;
Encerre o programa com uma mensagem; 
"""

notes = []

while True:

    try:
        value = float(input("enter a note(-1 for exit): "))
    except ValueError:
        print("invalid data type")

    if value == -1:
        break
    else:
        notes.append(value)

print(f"\nnumber of values read: {len(notes)}")
print(f"values in order: {notes}")

notes.reverse()

print("values in inverted order: ")
for note in notes:
    print(note)

print(f"sum of values: {sum(notes):.2f}")

average = sum(notes) / len(notes)

print(f"average of values: {average:.2f}")

above_average = 0
for note in notes:
    if note > average:
        above_average += 1

print(f"number of values above the average: {above_average:.0f}")

below_seven = 0
for note in notes:
    if note < 7:
        below_seven += 1

print(f"number of values below seven: {below_seven:.0f}")

print("end of program")