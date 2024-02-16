"""Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’, se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo"""

def positive_or_negative(n):
    if n > 0:
        return "p"
    else:
        return "n"
    
try:
    n = int(input("inform an integer: "))
except ValueError:
    print("invalid data type")

print(f"the value reported is {positive_or_negative(n)}")
