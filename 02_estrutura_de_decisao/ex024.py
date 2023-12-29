"""Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o número é:

    par ou ímpar;
    positivo ou negativo;
    inteiro ou decimal. """

num1 = float(input("enter a number: "))
num2 = float(input("enter other number: "))

operation = int(input("\ninfome the number refer a operation:\n1 - even or odd\n2 - integer or decimal\n3 - positive or negative\n"))

if operation == 1:
    # even or odd
    if num1 % 2 == 0:
        print(f"{num1} is a even number")
    else:
        print(f"{num1} is a odd number")

    if num2 % 2 == 0:
        print(f"{num2} is a even number")
    else:
        print(f"{num2} is a odd number")


elif operation == 2:
    # integer or decimal
    if num1 == round(num1):
        print(f"{num1} is a integer")
    else:
        print(f"{num1} is a decimal number")

    if num2 == round(num2):
        print(f"{num2} is a integer")
    else:
        print(f"{num2} is a decimal number")


elif operation == 3:
    # positive or negative 
    if num1 >= 0:
        print(f"{num1} is a positive number")
    else:
        print(f"{num1} is a negative number")
    
    if num2 >= 0:
        print(f"{num2} is a positive number")
    else:
        print(f"{num2} is a negative number")


else:
    print("invalid operation")