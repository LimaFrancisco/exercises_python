"""Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. Foram obtidos os seguintes dados:

    Código da cidade;
    Número de veículos de passeio (em 1999);
    Número de acidentes de trânsito com vítimas (em 1999). Deseja-se saber:
    Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
    Qual a média de veículos nas cinco cidades juntas;
    Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio. """

cod = [] * 5
vehicle = [] * 5
traffic_accident = [] * 5

higher_accident_rate = 0
lower_accident_rate = 0
vehicle_average = 0
accident_average = 0
count = 0

for index in range(0, 5):
    cod.insert(index, int(input("enter the code of the city: ")))
    vehicle.insert(index, int(input("enter the quantity of vehicles: ")))
    traffic_accident.insert(index, int(input("enter a quantity of accidents: ")))

    vehicle_average += traffic_accident[index]

    if vehicle[index] < 2000:
        accident_average += traffic_accident[index]
        count += 1

    if traffic_accident[index] == 0 or traffic_accident[index] <  lower_accident_rate:
        lower_accident_rate = index

    if traffic_accident[index] > higher_accident_rate:
        higher_accident_rate = index

vehicle_average = vehicle_average / 5

accident_average = accident_average / count

print(f"\ncities with higher and lower index of accidents:\nhigher: cod {cod[higher_accident_rate]} number of accidents {traffic_accident[higher_accident_rate]}\nlower: cod {cod[lower_accident_rate]} number of accidents {traffic_accident[lower_accident_rate]}")

print(f"\naverage number of vehicles in the 5 cities: {vehicle_average:.2f} ")

print(f"\naverage number of traffic accidents in cities with less than 2,000 vehicles: {accident_average:.2f}")
