# Escreva um programa que:
# • Leia (ou gere aleatoriamente) uma matriz quadrada de ordem N contendo elementos
# inteiros (N será lido);
# • Exiba a matriz lida (no formato de matriz);
# • Exiba os elementos da diagonal principal, isto é, os elementos onde I = J.
import random

n = int(input())
matriz = []
for i in range(n):
    linha = []
    for j in range(n):
        valor = random.randint(1, 100)
        linha.append(valor)
    matriz.append(linha)
    

for linha in matriz:
    print(linha)

print()
print() 


for i in range(n):
    print(matriz[i][i])
