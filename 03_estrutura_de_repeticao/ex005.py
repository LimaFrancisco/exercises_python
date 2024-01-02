"""Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação."""

countryA = int(input("population of country A: "))
countryB = int(input("population of country B: "))

growthA = float(input("country A growth percentage: "))
growthB = float(input("country B growth percentage: "))

years = 0 

while countryA < countryB:
    countryA += countryA * (growthA / 100)
    countryB += countryB * (growthB / 100)

    years += 1

print(f"{years} years")