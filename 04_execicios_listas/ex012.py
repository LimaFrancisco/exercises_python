"""Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos."""

ages = []
hights = []

average = 0
lower_average = 0

for index in range(0, 30):

    try:
        ages.append(int(input("enter the student`s age: ")))
        hights.append(float(input("now, enter the student`s hight: ")))
    except ValueError:
        print("invalid value")
        continue

    average += ages[index]

try:
    average = average / 30
except ZeroDivisionError:
    print("No students were entered")
    exit()

for index in range(0, 30):
    if ages[index] > 13 and hights[index] < average:
        lower_average += 1

print(f"{lower_average:.0f} students over 13 years old are below average height")