"""Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais número ele é divisível. """

num = int(input("enter a number: "))
prime = 0
message = ""

for index in range(1, (num + 1)):        
    if num % index == 0:
        prime += 1
        message += (f"\ndivisible by {index}")
    
if prime  == 2 :
    print("is a prime number")
else:
    print("is not a prime number" + message)
            