"""Data por extenso. Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário e imprima a data com o nome do mês por extenso. 
Data de Nascimento: 29/10/1973
Você nasceu em  29 de Outubro de 1973.
"""
date = input("date of birth: ")
formatted_date = ""
months = ("January","February","March","April","May","June","July","August","September","October","November","December")

day = ""

match int(date[1:2]):

    case 1:
        day = date[0:2] + "st"
    case 2:
        day = date[0:2] + "nd"
    case 3:
        day = date[0:2] + "rd"
    case _:
        day = date[0:2] + "th"

for item in range(0, 12):
    if int(date[3:5]) == (item + 1):
        formatted_date += months[item + 1] + " " + day + ", " + date[6:]

print(f"You were born on {formatted_date}")