# Encontrar o Máximo e o Mínimo
# Crie uma matriz 3x3 e encontre o maior e o menor valor presente na matriz.

matriz = [[0]*3 for i in range(3)]
maior = 0
menor = 99999999999999999999
for i in range(3):
    for j in range(3):
        matriz[i][j] = int(input())
        if matriz[i][j] > maior:
            maior = matriz[i][j]
        if matriz[i][j] < menor:
            menor = matriz[i][j]

for l in matriz:
    print(l)

print(f"Maior valor encontrado na matriz: {maior}")
print(f"Menor valor encontrado na matriz: {menor}")
