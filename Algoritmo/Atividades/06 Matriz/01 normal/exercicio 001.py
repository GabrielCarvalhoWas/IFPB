# Escreva um programa que preencha duas matrizes (A e B), ambas de ordem 2x3, com
# valores inteiros fornecidos pelo usuário (ou gerados aleatoriamente). O programa
# deverá somar as duas matrizes, armazenando o resultado em uma terceira matriz (C).
# Ao final, exiba as 3 matrizes (no formato de matriz).


matrizA = []
matrizB = []


for i in range(2):
    linha = []
    for j in range(3):
        coluna = int(input("digite 1: "))
        linha.append(coluna)
    matrizA.append(linha)


for i in range(2):
    linha = []
    for j in range(3):
        coluna = int(input("digite 2: "))
        linha.append(coluna)
    matrizB.append(linha)

matrizC = []

for i in range(2):
    linha = []
    for j in range(3):
        soma = matrizA[i][j] + matrizB[i][j]
        linha.append(soma)
    matrizC.append(linha)

for linha in matrizA:
    print(linha)
print()
for linha in matrizB:
    print(linha)
print()
for linha in matrizC:
    print(linha)