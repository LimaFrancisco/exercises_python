"""Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando o fatorial a números inteiros positivos e menores que 16. """

flag = "y"

while flag == "y":

    flag = input("want to perform the factorial calculation(y/n)")
    flag.lower()

    if flag == "y":
        n = int(input("enter a number: "))

        if n > 0 and n <= 16:
            result = 1 

            for index in range(1, n + 1):
                result *= index

            print(f"fat of {n} = {result}")
    
        else:
            print("invalid value")
    elif flag == "n":
        print("finished")