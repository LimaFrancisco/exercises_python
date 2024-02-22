"""Data com mês por extenso. Construa uma função que receba uma data no formato DD/MM/AAAA e devolva uma string no formato D de mesPorExtenso de AAAA. Opcionalmente, valide a data e retorne NULL caso a data seja inválida. """

from datetime import datetime

def date_in_full(date):
    try:
        valid_date = datetime.strptime(date, '%d/%m/%Y')
        months = ['January', 'February', 'March', 'April', 'May', 'June', 
                  'July', 'August', 'September', 'October', 'November', 'December']
        month_in_full = months[valid_date.month - 1]
        return f"{valid_date.day} of {month_in_full} of {valid_date.year}"
    except ValueError:
        return None

# Test the function
print(date_in_full(input("enter a valid date: "))) 
