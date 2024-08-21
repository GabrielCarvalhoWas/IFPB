# Matriz Transposta
# Dada uma matriz 2x3, crie uma nova matriz que seja a transposta da matriz original.

matriz = [[0]*3 for i in range(2)]
for i in range(2):
    for j in range(3):
        matriz[i][j] = int(input())

print(F"Matriz original:")
for linha in matriz:
    print(linha)

print()

matrizTransposta = [[0]*2 for i in range(3)]

for i in range(2):
    for j in range(3):
        matrizTransposta[j][i] = matriz[i][j]
print(f"Matriz transposta:")
for linha in matrizTransposta:
    print(linha)

