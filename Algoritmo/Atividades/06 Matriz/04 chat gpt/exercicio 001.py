# 
#

matriz = [[0]*3 for i in range(3)]

for i in range(3):
    for j in range(3):
        matriz[i][j] = 0
        if i == 2 or j == 1:
            matriz[i][j] = 1

for l in matriz:
    print(l)