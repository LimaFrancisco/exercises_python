"""Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:

    "Telefonou para a vítima?"
    "Esteve no local do crime?"
    "Mora perto da vítima?"
    "Devia para a vítima?"
    "Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente"."""


veredict = 0

# first question
response = input("did you call the victim? ") 
response.lower()

if response[0] == "s":
    veredict += 1

# second question
response = input("were you at the scene of the crime? ") 
response.lower()

if response[0] == "s":
    veredict += 1

# third question
response = input("do you live near the victim? ") 
response.lower()

if response[0] == "s":
    veredict += 1

# fourth question
response = input("owed to the victim? ") 
response.lower()

if response[0] == "s":
    veredict += 1

# fifth question
response = input("have you worked with the victim? ") 
response.lower()

if response[0] == "s":
    veredict += 1


# calculating the result
if veredict <= 1:
    print("innocent")
elif veredict == 2:
    print("suspect")
elif veredict == 3 or veredict == 4:
    print("accomplice")
elif veredict == 5:
    print("guilty")