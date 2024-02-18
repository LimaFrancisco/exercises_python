"""Faça um programa que converta da notação de 24 horas para a notação de 12 horas. Por exemplo, o programa deve converter 14:25 em 2:25 P.M. A entrada é dada em dois inteiros. Deve haver pelo menos duas funções: uma para fazer a conversão e uma para a saída. Registre a informação A.M./P.M. como um valor ‘A’ para A.M. e ‘P’ para P.M. Assim, a função para efetuar as conversões terá um parâmetro formal para registrar se é A.M. ou P.M. Inclua um loop que permita que o usuário repita esse cálculo para novos valores de entrada todas as vezes que desejar"""

def converting_hour(hour, minute):
    if hour > 12:
        return f"{hour-12}:{minute} P.M"
    else:
        return f"{hour}:{minute} A.M"
    
hour = 0
minute = 0 

while True:

    try:
        value = int(input("enter the hour:(end=-1) "))

        if value >= 0 and value < 24:
            hour = value
        else:
            print("invalid hour")

        value = int(input("enter the minutes:(end=-1) "))

        if value >= 0 and value < 60:
            minute = value
        else:
            print("invalid minute")

    except ValueError:
        print("invalid data type")

    if hour == -1 or minute == -1:
        exit()

    print(converting_hour(hour, minute))