# Escreva um programa que receba um vetor V de N números inteiros (N será lido),
# determine e exiba o maior e o menor elemento deste vetor e seus respectivos
# índices.
# Obs: suponha a inexistência de valores repetidos.

n = int(input())
vetor = [0] * n

for i in range(n):
    vetor[i] = int(input())

maxTamanho = vetor[0]
minTamanho = vetor[0]
maiorIndice = 0
menorIndice = 0

for e in range(n):
    if vetor[e] > maxTamanho:
        maxTamanho = vetor[e]
        maiorIndice = e
    if vetor[e] < minTamanho:
        minTamanho = vetor[e]
        menorIndice = e

print(f"Vetor total: {vetor}")  
print(f"Maior vetor: {maxTamanho} e seu índice: {maiorIndice}")
print(f"Maior vetor: {minTamanho} e seu índice: {menorIndice}")  
