"""Tamanho de strings. Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento. Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo. 
Compara duas strings
String 1: Brasil Hexa 2006
String 2: Brasil! Hexa 2006!
Tamanho de "Brasil Hexa 2006": 16 caracteres
Tamanho de "Brasil! Hexa 2006!": 18 caracteres
As duas strings são de tamanhos diferentes.
As duas strings possuem conteúdo diferente.
"""
try:
    string1 = input("enter any string: ")
    string2 = input("enter another string: ")
except ValueError:
    print("invalid data type")

print(f"String 1: {string1}")
print(f"String 2: {string2}")

print(f"Size of \"{string1}\": {len(string1)} characters")
print(f"Size of \"{string2}\": {len(string2)} characters")

if len(string1) == len(string2):
    print("strings have equal lengths")
else:
    print("strings have diferent lengths")

if string1 == string2:
    print("strings have equal contents")
else:
    print("strings have diferent contents")  
