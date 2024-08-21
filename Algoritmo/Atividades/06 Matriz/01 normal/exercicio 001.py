# Escreva um programa que preencha duas matrizes (A e B), ambas de ordem 2x3, com
# valores inteiros fornecidos pelo usuário (ou gerados aleatoriamente). O programa
# deverá somar as duas matrizes, armazenando o resultado em uma terceira matriz (C).
# Ao final, exiba as 3 matrizes (no formato de matriz).

import random 

matrizA = []
matrizB = []

for i in range(2):
    linha = []
    for j in range(3):
        valor = random.randint(1,100)
        linha.append(valor)
    matrizA.append(linha)

for i in range(2):
    linha = []
    for j in range(3):
        valor = random.randint(1,100)
        linha.append(valor)
    matrizB.append(linha)

matriz_C = []

for i in range(2):
    linha = []
    for j in range(3):
        soma = matrizA[i][j] + matrizB[i][j]
        linha.append(soma)
    matriz_C.append(linha)


for linha in matrizA:
    print(linha)


print()
print()


for linha in matrizB:
    print(linha)

print()
print()

for linha in matriz_C:
    print(linha)