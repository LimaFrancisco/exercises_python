"""Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida."""

age = []
hight = []

for index in range(0, 5):

    try:
        age.append(int(input("enter an age or a person: ")))
        hight.append(float(input("now enter your hight: ")))
    except ValueError:
        print("invalid value")

age.reverse()
hight.reverse()

print(f"\nlist of ages inverted: {age}")
print(f"list of hights inverted: {hight}")