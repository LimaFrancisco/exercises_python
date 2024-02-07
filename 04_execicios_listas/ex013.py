"""Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ). """

def get_month(month):
    months = [
        "January", "February", "March", "April",
        "May", "June", "July", "Agust",
        "Setember", "October", "November", "December"
    ]
    return months[month - 1]

temperatures = []
for month in range(1, 13):

    try:
        temperature = float(input(f"inform the average temperature of {get_month(month)}: "))
        temperatures.append(temperature)
    except ValueError:
        print("data type invalid")

media_anual = sum(temperatures) / len(temperatures)

print("\ntemperatures above the annual average:")
for month, temperature in enumerate(temperatures):
    if temperature > media_anual:
        print(f"{get_month(month + 1)}: {temperature:.2f}°C")

