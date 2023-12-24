"""Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido. """

gender = input("enter M for male or F female: ")

gender.lower()

if gender == "m":
    print("M - Male")
elif gender == "f":
    print("F - Female")