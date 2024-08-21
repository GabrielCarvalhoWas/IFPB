# Achar elementos da matriz secundaria

matriz = [[None]* 3 for i in range(3)]
secundaria = []
for i in range(3):
    for j in range(3):
        matriz[i][j] = int(input())
        if i + j == 3 - 1:
            secundaria.append(matriz[i][j])
    
for l in matriz:
    print(l)

print()

print(secundaria)

        