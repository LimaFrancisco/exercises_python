"""Faça um Programa que verifique se uma letra digitada é vogal ou consoante. """

letter = input("enter a letter: ")

letter = letter.lower()

if letter in ('a', 'e', 'i', 'o', 'u'):
    print("vowel")
elif letter in ('b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'):
    print("consoant")