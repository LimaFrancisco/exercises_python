"""Sendo H= 1 + 1/2 + 1/3 + 1/4 + ... + 1/N, Faça um programa que calcule o valor de H com N termos. """

n = 2
m = 1

serie = "H = 1 + "

su = 1

num = int(input("enter a integer: "))

while n <= num:
    su =+ m / n

    if n < num:
      serie =  serie + (str(m) + "/" + str(n) + " + ")
    elif n == num:
       serie =  serie + (str(m) + "/" + str(n))

    n += 1

print(f"\nsum = {su:.2f}")
print(serie)