"""A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... Faça um programa que gere a série até que o valor seja maior que 500. """
fibonacci = [0, 1]

for index in range(2 , 100):
    next = fibonacci[index - 1] + fibonacci[index - 2]
    fibonacci.append(next)
    if next > 500:
        break

print(f"fibonacci up to the first number greater than 500: {fibonacci}")