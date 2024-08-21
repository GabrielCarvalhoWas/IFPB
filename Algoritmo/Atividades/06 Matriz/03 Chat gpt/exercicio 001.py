# Criar e Exibir uma Matriz
# Crie uma matriz 3x3 e exiba seus elementos. Cada elemento pode ser um número inteiro ou um valor definido por você.

matriz = [[0]*3 for i in range(3)]
for i in range(3):
    for j in range(3):
        matriz[i][j] = int(input())
for l in matriz:
    print(l)