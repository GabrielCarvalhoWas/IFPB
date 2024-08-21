# Escreva um programa que:
# • Leia uma matriz M de ordem 20 x 50 contendo valores inteiros;
# • Leia um valor inteiro K;
# • Imprima todas as posições (linha e coluna) em que se encontra o valor K dentro da matriz M.

import random 

matrizM = [[None]*50 for i in range(20)]
k = int(input())
encontrado = False
for i in range(20):
    for j in range(50):
        matrizM[i][j] = random.randint(1, 100)
        if k == matrizM[i][j]:
            print(f"Valor {k} encontrado na posição na linha {i} e coluna {j}")
            encontrado = True
if not encontrado:
    print(f"Valor {k} não encontrado em nenhumna posição")


