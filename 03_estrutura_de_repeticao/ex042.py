"""Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100]. A entrada de dados deverá terminar quando for lido um número negativo. """

flag = 0

count1 = 0
count2 = 0
count3 = 0
count4 = 0

while flag >= 0:

    flag = int(input("enter a positive number(or negative for exit): "))

    if flag >= 0 and flag <= 25:
        count1 += 1
    elif flag >= 26 and flag <= 50:
        count2 += 1
    elif flag >= 51 and flag <= 75:
        count3 += 1
    elif flag >= 76 and flag <= 10:
        count4 += 1

print(f"\nfinal result\n{count1:.0f} numbers between 0-25\n{count2:.0f} numbers between 26-50\n{count1:.0f} numbers between 51-75\n{count1:.0f} numbers between 76-100")