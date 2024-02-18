"""Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado"""

def digits_number(value):
    return len(str(value))

try:
    value = int(input("enter any integer: "))
except ValueError:
    print("invalid data type")

print(f"{digits_number(value)} digits")