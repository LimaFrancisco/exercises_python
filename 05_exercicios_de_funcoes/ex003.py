"""Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos."""

def sum_of_three(n1,n2,n3):
    return n1+n2+n3

print("enter three integers: ")

try:
    n1 = int(input())
    n2 = int(input())
    n3 = int(input())
except ValueError:
    print("invalid data type")
    exit()

print(f"the sum of the values is {sum_of_three(n1,n2,n3)}")