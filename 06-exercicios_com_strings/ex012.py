"""Valida e corrige número de telefone. Faça um programa que leia um número de telefone, e corrija o número no caso deste conter somente 7 dígitos, acrescentando o '3' na frente. O usuário pode informar o número com ou sem o traço separador. 
Valida e corrige número de telefone
Telefone: 461-0133
Telefone possui 7 dígitos. Vou acrescentar o digito três na frente.
Telefone corrigido sem formatação: 34610133
Telefone corrigido com formatação: 3461-0133
"""

fone = input("enter a fone number: ")
formatted_fone = fone.replace("-","")

print(f"fone: {fone}")

if len(formatted_fone) == 7:
    print("the fone have 7 digits. I will add the digit 3 in front.")
    
    formatted_fone = '3' + formatted_fone
    print(f"Fixed phone without formatting: {formatted_fone}")
    fone = '3' + formatted_fone
    print(f"Fixed phone with formatting: {fone}")
