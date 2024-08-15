# Uma matriz transposta é a matriz que se obtém da troca de linhas por colunas de uma
# dada matriz.
# Assim, dada uma matriz C de ordem m x n, a matriz transposta dela será representada
# por Ct de ordem n x m, onde cada elemento de Ct[i,j] = C[j,i].

# Escreva um programa que preencha uma matriz 3x5 com valores inteiros fornecidos
# pelo usuário (ou gerados aleatoriamente) e gere a sua transposta. Ao final, imprima as
# duas matrizes (no formato de matriz).


matriz = []

for i in range(3):
    linha = []
    for j in range(5):
        coluna = int(input())
        linha.append(coluna)
    matriz.append(linha)


for linha in matriz:
    print(linha)
print()
matriz02 = []

for j in range(5):
    linha = []
    for i in range(3):
        linha.append(matriz[i][j])
    matriz02.append(linha)

for linha in matriz02:
    print(linha)