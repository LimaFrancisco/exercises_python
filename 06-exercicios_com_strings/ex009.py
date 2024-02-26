"""Verificação de CPF. Desenvolva um programa que solicite a digitação de um número de CPF no formato xxx.xxx.xxx-xx e indique se é um número válido ou inválido através da validação dos dígitos verificadores edos caracteres de formatação. """

import re

def calculate_digit(cpf, start, end, weight):
    sum = 0
    for i in range(start, end):
        sum += int(cpf[i]) * (weight - i)
    sum = 11 - sum % 11
    return sum if sum <= 9 else 0

def validate_cpf(cpf):
    cpf = re.sub(r'\D', '', cpf)
    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False
    first_digit = calculate_digit(cpf, 0, 9, 10)
    second_digit = calculate_digit(cpf, 0, 10, 11)
    return cpf[-2:] == f"{first_digit}{second_digit}"

def main():
    cpf = input("Please enter your CPF in the format xxx.xxx.xxx-xx: ")
    if validate_cpf(cpf):
        print("The CPF number is valid.")
    else:
        print("The CPF number is invalid.")

if __name__ == "__main__":
    main()
