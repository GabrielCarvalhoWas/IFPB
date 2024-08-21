import random
n = int(input())
matriz = [[None]*n for i in range(n)]
maior = -999999
menor = 99999999
for i in range(n):
    for j in range(n):
        matriz[i][j] = random.randint(1, 10)
        if i == j:
            if matriz[i][j] > maior:
                maior = matriz[i][j]
        if i + j == n - 1:
            if matriz[i][j] < menor:
                menor = matriz[i][j]

media = (menor + maior) / 2

for l in matriz:
    print(l)

print()
print(maior)
print(menor)
print(media)

