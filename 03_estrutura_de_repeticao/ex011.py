"""Altere o programa anterior para mostrar no final a soma dos números. """

num1 = int(input("enter a integer: "))
num2 = int(input("enter another integer: "))

start = 0
end = 0

sum = 0

if num1 > num2:
    start = num2 + 1
    end = num1
elif num2 > num1:
    start = num1 + 1
    end  = num2

for index in range(start, end):
    print(index)
    sum += index

print(f"\nsum betwen all numbers: {sum}")