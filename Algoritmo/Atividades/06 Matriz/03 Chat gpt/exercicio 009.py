# Matriz Diagonal
# Crie uma matriz 4x4 onde apenas os elementos da diagonal principal são diferentes de zero e todos os outros elementos são zero.
import random
matriz = [[0]*4 for i in range(4)]
for i in range(4):
    for j in range(4):
        matriz[i][i] = random.randint(1, 100)

for l in matriz:
    print(l)
