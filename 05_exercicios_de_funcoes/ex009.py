"""Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721. """

def reversing(value):
    value = str(value)
    newValue = ""

    for index in range(len(value) - 1, -1, -1):
        newValue = newValue + value[index]

    return int(newValue)

try:
    value = int(input("enter any integer: "))
except ValueError:
    print("invalid data type")
    exit()

reversing(value)

print(f"{reversing(value)}")