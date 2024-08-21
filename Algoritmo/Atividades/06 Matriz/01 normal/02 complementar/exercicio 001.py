# Uma matriz de permutação é uma matriz quadrada cujos elementos são 0's
# ou 1's, tal que em cada linha e em cada coluna exista apenas um elemento
# igual a 1. Por exemplo, a matriz seguinte é uma matriz de permutação.


n = int(input())
matriz = [[None]*n for i in range(n)]
for i in range(n):
    for j in range(n):
        matriz[i][j] = 0
        if i == j:
            matriz[i][j] = 1

for l in matriz:
    print(l)