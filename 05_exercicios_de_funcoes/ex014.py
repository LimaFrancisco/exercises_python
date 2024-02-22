"""Quadrado mágico. Um quadrado mágico é aquele dividido em linhas e colunas, com um número em cada posição e no qual a soma das linhas, colunas e diagonais é a mesma. Por exemplo, veja um quadrado mágico de lado 3, com números de 1 a 9: 
8  3  4 
1  5  9
6  7  2
Elabore uma função que identifica e mostra na tela todos os quadrados mágicos com as características acima. Dica: produza todas as combinações possíveis e verifique a soma quando completar cada quadrado. Usar um vetor de 1 a 9 parece ser mais simples que usar uma matriz 3x3. 
"""

import numpy as np
from itertools import permutations

def is_magic_square(square):
    s = np.sum(square[0])
    return all(np.sum(row) == s for row in square) and all(np.sum(square[:,i]) == s for i in range(3)) and np.sum(square.diagonal()) == s and np.sum(np.fliplr(square).diagonal()) == s

def generate_magic_squares():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for perm in permutations(numbers):
        square = np.array(perm).reshape(3, 3)
        if is_magic_square(square):
            print(square)
            print()

generate_magic_squares()
