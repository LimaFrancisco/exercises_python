"""Leet spek generator. Leet é uma forma de se escrever o alfabeto latino usando outros símbolos em lugar das letras, como números por exemplo. A própria palavra leet admite muitas variações, como l33t ou 1337. O uso do leet reflete uma subcultura relacionada ao mundo dos jogos de computador e internet, sendo muito usada para confundir os iniciantes e afirmar-se como parte de um grupo. Pesquise sobre as principais formas de traduzir as letras. Depois, faça um programa que peça uma texto e transforme-o para a grafia leet speak. """

newWord = ""

alphabet = {"a" : "4",
            "b" : "13",
            "c" : "(",
            "d" : "[)",
            "e" : "3",
            "f" : "|=",
            "g" : "6",
            "h" : "|-|",
            "i" : "|",
            "j" : ".]",
            "k" : "|<",
            "l" : "1",
            "m" : "|Y|",
            "n" : "N",
            "o" : "0",
            "p" : "|>",
            "q" : "0,",
            "r" : "|2",
            "s" : "5",
            "t" : "7",
            "u" : "[_]",
            "v" : "V",
            "w" : "\\v/",
            "x" : "}{",
            "y" : "`/",
            "z" : "2"}

word = input("enter any word: ")
word.lower()

word = list(word)

for index in range(0, len(word)):
    if word[index] in alphabet:
        word[index] = alphabet[word[index]]
    else:
        word[index] = word[index]

word = "".join(word)

print(f"\n{word}\n")