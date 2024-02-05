"""Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores. """

first_vector = []
second_vector = []

interleaved = [] * 20

try:
    for index in range(0, 10):
        first_vector.append(int(input("enter and interger for a first list: ")))

    for index in range(0, 10):
        second_vector.append(int(input("enter and interger for a second list: ")))
except ValueError:
    print("invalid value")

for index in range(0, 10):
        interleaved.append(first_vector[index])
        interleaved.append(second_vector[index])

print(f"\nvalues of first list: {first_vector}")
print(f"values of second list: {second_vector}")
print(f"values interleaved: {interleaved}")