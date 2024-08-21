# Achar elementos da diagonal principal

matriz = [[None]*3 for i in range(3)]
diagonal = []
for i in range(3):
    for j in range(3):
        matriz[i][j] = int(input())
        if i == j:
            diagonal.append(matriz[i][j])

for l in matriz:
    print(l)
print()
print(diagonal)