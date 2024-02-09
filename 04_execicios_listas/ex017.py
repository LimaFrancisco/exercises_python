"""Em uma competição de salto em distância cada atleta tem direito a cinco saltos. O resultado do atleta será determinado pela média dos cinco valores restantes. Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois informe o nome, os saltos e a média dos saltos. O programa deve ser encerrado quando não for informado o nome do atleta. A saída do programa deve ser conforme o exemplo abaixo: 
Atleta: Rodrigo Curvêllo
 
Primeiro Salto: 6.5 m
Segundo Salto: 6.1 m
Terceiro Salto: 6.2 m
Quarto Salto: 5.4 m
Quinto Salto: 5.3 m

Resultado final:
Atleta: Rodrigo Curvêllo
Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
Média dos saltos: 5.9 m
"""

name = input("Enter the athlete's name: ")
jumps = []

average = 0

for index in range(0, 5):
    try:
        jumps.append(float(input("enter the jump distance: " )))
    except ValueError:
        print("invalid data type")
        continue

    average += jumps[index]

average = average / len(jumps)

print("\nfinal result:")
print(f"athlete: {name}")
print(f"jumps: {jumps}")
print(f"jump average: {average} m")
