"""Faça um programa que mostre os n termos da Série a seguir:

      S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m. 

    Imprima no final a soma da série. """

n = 1
m = 1

serie = "S = "

su = 0

num = int(input("enter a integer: "))

while n <= num:
    su =+ n / m

    if n < num:
      serie =  serie + (str(n) + "/" + str(m) + " + ")
    elif n == num:
       serie =  serie + (str(n) + "/" + str(m))

    n += 1
    m += 2

print(f"\nsum = {su:.2f}")
print(serie)