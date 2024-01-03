"""A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n−ésimo termo. """

n = int(input("enter a integer: "))

fibonacci = [0, 1]

for index in range(2 , n):
    next = fibonacci[index - 1] + fibonacci[index - 2]
    fibonacci.append(next)

print(f"{n} first numbers of the fibonacci sequence are: {fibonacci}")