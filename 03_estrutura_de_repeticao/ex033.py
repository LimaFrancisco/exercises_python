"""O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as um conjunto indeterminado de temperaturas, e informe ao final a menor e a maior temperaturas informadas, bem como a média das temperaturas."""

temperatures = []

while True:
    temp = input("report a temperature (or 'exit' to end): ")

    if temp.lower() == 'exit':
        break
    else:
        try:
            temperatures.append(float(temp))
        except ValueError:
            print("please, enter a valid number.")

if temperatures:
    print(f"the lowest temperature is: {min(temperatures)}")
    print(f"the highest temperature is: {max(temperatures)}")
    print(f"the average temperature is: {sum(temperatures) / len(temperatures)}")
else:
    print("no temperature was entered.")