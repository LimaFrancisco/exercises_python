"""Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto"""

year = int(input("enter a random year: "))

leap_year = False

if year % 4 == 0:
    leap_year = True
    if year % 100 == 0:
        leap_year = False
        if year % 400 == 0:
            leap_year = True

if leap_year == True:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")