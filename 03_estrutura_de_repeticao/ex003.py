"""Faça um programa que leia e valide as seguintes informações:

    Nome: maior que 3 caracteres;
    Idade: entre 0 e 150;
    Salário: maior que zero;
    Sexo: 'f' ou 'm';
    Estado Civil: 's', 'c', 'v', 'd'; """

while True:
    name = input("enter your name: ")

    if len(name) > 3:
        break
    else:
        print("invalid name, try again... ")

while True:
    age = int(input("enter your age: "))

    if age > 0 and age <= 150:
        break
    else:
        print("invalid age, try again...")

while True:
    salary = float(input("enter your salary: "))

    if salary > 0:
        break
    else:
        print("invalid salary, try again...")

while True:
    sex = input("enter your sex(f or m): ")
    sex.lower()

    if sex == "f" or sex == "m":
        break
    else:
        print("invalid sex, try again...")

while True:
    marital_state = input("enter your marital state(s, c, v, d): ")
    marital_state.lower()

    if marital_state == "s" or marital_state == "c" or marital_state == "v" or marital_state == "d":
        break
    else:
        print("marital state invalid, try again...")
