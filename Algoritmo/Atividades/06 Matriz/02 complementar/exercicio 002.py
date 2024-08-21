# Uma matriz quadrada contendo valores inteiros é denominada quadrado
# mágico quando a soma dos elementos de cada linha, a soma dos elementos
# de cada coluna e a soma dos elementos das diagonais principal e secundária
# são todos iguais. Por exemplo, a matriz seguinte é um quadrado mágico.
# 8 0 7
# 4 5 6
# 3 10 2
# Escreva um programa que preencha uma matriz com valores fornecidos pelo
# usuário, determine e mostre se ela é um quadrado mágico.
n = int(input())
matriz = [[0]*n for i in range(n)]

for i in range(n):
    for j in range(n):
        matriz[i][j] = int(input("Digite um valor: "))
