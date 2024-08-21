# Inversão de Linha e Coluna
# Dada uma matriz 3x3, inverta a ordem das linhas e das colunas.

matrizA = [[0]*3 for i in range(3)]
for i in range(3):
    for j in range(3):
        matrizA[i][j] = int(input())
for l in matrizA:
    print(l)

matrizB = [[0]*3 for i in range(3)]

for i in range(3):
    for j in range(3):
        matrizB[i][j] = matrizA[2-i][2-j]

print()
for l in matrizB:
    print(l)