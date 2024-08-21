# Soma dos Elementos de uma Matriz
# Crie uma matriz 4x4 e calcule a soma de todos os seus elementos.
matriz =[[0]*4 for i in range(4)]
soma = 0
for i in range(4):
    for j in range(4):
        matriz[i][j] = int(input())
        soma += matriz[i][j]
for l in matriz:
    print(l)

print()
print(f"Sua soma: {soma}")