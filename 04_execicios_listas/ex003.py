"""Faça um Programa que leia 4 notas, mostre as notas e a média na tela"""

notes = [] * 4
su = 0

for index in range(0, 4):
    notes.append(float(input("enter a student note: ")))
    su += notes[index]

su = su / 4

print(f"student`s notes: {notes}\nnote average: {su:.2f}")