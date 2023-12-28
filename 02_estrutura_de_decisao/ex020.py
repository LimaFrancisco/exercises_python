"""Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e presentar:

    A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
    A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
    A mensagem "Aprovado com Distinção", se a média for igual a 10. """

print("report a student's three partial grades: ")
grade1 = float(input())
grade2 = float(input())
grade3 = float(input())

average = (grade1 + grade2 + grade3) / 3

if average == 10:
    print("approved with distinction")
elif average >= 7:
    print("approved")
elif average < 7:
    print("disapproved")