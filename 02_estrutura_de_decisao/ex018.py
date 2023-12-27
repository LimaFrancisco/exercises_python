"""Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida."""

date = input("enter a date in format dd/mm/yyyy: ")
# string index                       0123456789

# let`s do it by steps
day = 0
month = 0
year = 0

# checking structure
if date[2] == "/" and date[5] == "/":

    # checking data types
    if date[0:2].isnumeric() and date[3:5].isnumeric() and date[6:].isnumeric():
        day = int(date[0:2])
        month = int(date[3:5])
        year = int(date[6:])

        if (day > 0 and day <= 31) and (month > 0 and month <= 12) and (year >= 0):
            print(f"{date} is a valid date")
        else:
            print(f"{date} is a invalid date")

    else:
        print(f"{date} is a invalid date")

else:
    print(f"{date} is a invalid date")