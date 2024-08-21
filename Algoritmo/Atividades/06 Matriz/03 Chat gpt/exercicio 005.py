# Soma das Diagonais
# Dada uma matriz quadrada 4x4, calcule a soma dos elementos da diagonal principal e da diagonal secundária.

matriz = [[0]*4 for i in range(4)]
diagonalPrincipal = diagonalSecundaria = 0
for i in range(4):
    for j in range(4):
        matriz[i][j] = int(input())
        if i == j:
            diagonalPrincipal += matriz[i][j]
        if i + j == 3:
            diagonalSecundaria += matriz[i][j]
for l in matriz:
    print(l)

print(f"Soma da diagonal Principal: {diagonalPrincipal}")
print(f"Soma da diagonal Secundária: {diagonalSecundaria}")
