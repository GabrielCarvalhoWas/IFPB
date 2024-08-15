# Escreva um programa que leia 10 números e armazene-os em um vetor. Exiba:
# Os números que estão nos índices pares;
# Os números que estão nos índices ímpares.
n = 10
vetor = [0] * n
for i in range(n):
    vetor[i] = int(input())

for e in range(0, n, 2):
    print(f"pares: {vetor[e]}")

for a in range(1, n, 2):
    print(f"impares {vetor[a]}")

