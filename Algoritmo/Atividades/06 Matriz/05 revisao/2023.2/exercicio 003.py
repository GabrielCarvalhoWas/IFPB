# Escreva um programa que:
# • Leia uma matriz quadrada de ordem 30 contendo números inteiros;
# • Gere e imprima um vetor que deverá conter os elementos da diagonal principal da matriz;
# • Gere e imprima um vetor que deverá conter os elementos da diagonal secundária da matriz.
import random
n = 30
matriz = [[None]*n for i in range(n)]
diagonalPrincipal = []
diagonalSecundaria = []
for i in range(n):
    for j in range(n):
        matriz[i][j] = random.randint(1, 100)
        if i == j:
            diagonalPrincipal.append(matriz[i][j])
        if i + j == n - 1:
            diagonalSecundaria.append(matriz[i][j])



print()

print(diagonalPrincipal)
print(diagonalSecundaria)


