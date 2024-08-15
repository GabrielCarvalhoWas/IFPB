# Escreva um programa que gere aleatoriamente uma matriz quadrada A (cuja ordem
# será lida) e gere uma matriz B (da mesma ordem de A), onde cada elemento de B
# corresponderá ao respectivo elemento de A somado a ele os seus índices, sendo que se
# o elemento for de alguma diagonal (principal ou secundária) deverá ser colocado 0
# (zero).
# Veja o exemplo a seguir:

# Ao final, imprima as duas matrizes (no formato de matriz).


import random



n = int(input())
matriz_A = []


for i in range(n):
    linha = []
    for j in range(n):
        valor = random.randint(1, 100)
        linha.append(valor)
    matriz_A.append(linha)

matriz_B = []

for i in range(n):
    linha = []
    for j in range(n):
        if i == j or j == n - 1:
            linha.append(0)
        else:
            valor = matriz_A[i][j] + i + j
            linha.append(valor)
    matriz_B.append(linha)

for linha in matriz_A:
    print(linha)

print()
print()
for linha in matriz_B:
    print(linha)