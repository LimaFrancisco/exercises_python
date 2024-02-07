"""Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:

    "Telefonou para a vítima?"
    "Esteve no local do crime?"
    "Mora perto da vítima?"
    "Devia para a vítima?"
    "Já trabalhou com a vítima?" 
    
    O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente". """

questions = ["Did you call the victim?","Were you at the scene of the crime?","Do you live near the victim?","Should it go to the victim?","Have you worked with the victim?"]
classification = 0

for index in range(0,5):
    answers = input(f"{questions[index]}(yes/no)").lower()

    if answers == "yes":
        classification += 1

match classification:

    case 2:
        print("suspect")
    case 3:
        print("accomplice")
    case 4:
        print("accomplice")
    case 5:
        print("assassin")
    case _:
        print("innocent")    
