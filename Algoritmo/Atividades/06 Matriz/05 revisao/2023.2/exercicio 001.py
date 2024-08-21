# Escreva um programa que:
# • Leia um valor inteiro N;
# • Leia um vetor A contendo N inteiros;
# • Gere e imprima um vetor B onde cada elemento de B será calculado com base no elemento de A
# da mesma posição usando a seguinte regra: se o elemento de A for par, o elemento de B será 0,
# e se o elemento de A for ímpar, o elemento de B será 1.
# Exemplo: N = 8, A = [7, 12, 15, 10, 4, 9, 3, 6], B = [1, 0, 1, 0, 0, 1, 1, 0]

n = int(input())
vetorA = [None] * n 
vetorB = [None] * n 
for i in range(n):
    vetorA[i] = int(input())
    if vetorA[i] % 2 == 0:
        vetorB[i] = 0
    else:
        vetorB[i] = 1



print(vetorA)
print(vetorB)
