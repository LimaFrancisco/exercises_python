"""Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso. """

shift = input("inform the shift you study(M, V, N): ")

shift = shift.lower()

if shift == 'm':
    print("good morning")
elif shift == 'v':
    print("good afternoon")
elif shift == 'n':
    print("good evernig")