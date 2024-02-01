"""Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões, o programa deve perguntar ao aluno a resposta de cada questão e ao final comparar com o gabarito da prova e assim calcular o total de acertos e a nota (atribuir 1 ponto por resposta certa). Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro aluno vai utilizar o sistema. Após todos os alunos terem respondido informar: 

Maior e Menor Acerto;
Total de Alunos que utilizaram o sistema;
A Média das Notas da Turma. 

Gabarito da Prova:

01 - A
02 - B
03 - C
04 - D
05 - E
06 - E
07 - D
08 - C
09 - B
10 - A

Após concluir isto você poderia incrementar o programa permitindo que o professor digite o gabarito da prova antes dos alunos usarem o programa. 
"""
template = []

for index in range(0, 10):
    response = (input(f"provide the answer to question {index + 1:.0f}(A,B,C,D,E): "))
    response = response.upper()

    if response == 'A' or response == 'B' or response == 'C' or response == 'C' or response == 'D' or response == 'E':
        template.append(response)
    else:
        print("invalid answer")

print(template)

student_template = []
note = 0

highest_note = 0
lowest_note = 0

student_number = 0

general_average = 0

while True:

    flag = input("do you want to register(Y/n)?")
    flag.lower()

    if flag == "y":

        student_number += 1
        note = 0

        for index in range(0, 10):

            answer = (input(f"provide the answer to question {index + 1:.0f}(A,B,C,D,E): "))
            answer = answer.upper()

            if answer == "A" or answer == "B" or answer == "C" or answer == "D" or answer == "E":
                student_template.append(answer)

                if answer == template[index]:
                    note += 1
            else:
                print("invalid response")

    elif flag == "n":
        break
    
    if note > highest_note:
        highest_note = note

    if lowest_note == 0 or note < lowest_note:
        lowest_note = note

    general_average += note

general_average = general_average / student_number

print(f"\nhighest average {highest_note:.2f}\nlowest average {lowest_note:.2f}\ntotal number of students {student_number:.0f}\nclass average {general_average:.2f}")