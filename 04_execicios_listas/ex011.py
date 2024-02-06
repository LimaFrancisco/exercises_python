"""Altere o programa anterior, intercalando 3 vetores de 10 elementos cada."""

first_vector = []
second_vector = []
third_vector = []

interleaved = [] * 30

try:
    for index in range(0, 10):
        first_vector.append(int(input("enter and interger for a first list: ")))

    for index in range(0, 10):
        second_vector.append(int(input("enter and interger for a second list: ")))

    for index in range(0, 10):
        third_vector.append(int(input("enter and interger for a third list: ")))

except ValueError:
    print("invalid value")

for index in range(0, 10):
        interleaved.append(first_vector[index])
        interleaved.append(second_vector[index])
        interleaved.append(third_vector[index])

print(f"\nvalues of first list: {first_vector}")
print(f"values of second list: {second_vector}")
print(f"values of third list: {third_vector}")
print(f"values interleaved: {interleaved}")