# Achar elementos abaixo da diagonal principal
n = 3
matriz = [[None]* n for i in range(n)]
DP = []
for i in range(n):
    for j in range(n):
        matriz[i][j] = int(input())
        if i > j:
            DP.append(matriz[i][j])

for l in matriz:
    print(l)

print()

print(DP)
