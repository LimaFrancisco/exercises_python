"""Desenha moldura. Construa uma função que desenhe um retângulo usando os caracteres ‘+’ , ‘−’ e ‘| ‘. Esta função deve receber dois parâmetros, linhas e colunas, sendo que o valor por omissão é o valor mínimo igual a 1 e o valor máximo é 20. Se valores fora da faixa forem informados, eles devem ser modificados para valores dentro da faixa de forma elegante. """

def frame(row, column):
    if row < 1 or row > 20:
        row = 10
    elif column < 1 or column > 20:
        column = 10

    list = []

    for index in range(0, row):
        if index == 0 or index == row -1:
            if column == 1:
                list.append("+")
            else:
                list.append("+" + ("-" * (column - 2)) + "+")
        else:
            if column == 1:
                list.append("|")
            else:
                list.append("|" + (" " * (column - 2)) + "|")

    return list

try:
    row = int(input("enter the number of lines: "))
    column = int(input("now, enter the number of columns: "))
except ValueError:
    print("invalid data type")

list = frame(row, column)

for item in list:
    print(item)