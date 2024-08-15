# Escreva um programa que leia um vetor de N números inteiros (N será lido),
# inverta a ordem dos elementos do vetor e exiba o vetor invertido.
# Ex: V = [1, 3, 5, 7], após a inversão: V = [7, 5, 3, 1].
# Obs: É necessário inverter os elementos do vetor, não basta imprimi-los em
# ordem inversa!

n = int(input("Digite o tamanho do vetor: "))
vetor = [0] * n

for i in range(n):
    vetor[i] = int(input(f"Digite o {i+1} elemento: "))

print(f"Tamanho original do vetor: {vetor}")

for e in range(n//2):
    subs = vetor[e]
    vetor[e] = vetor[n-e-1]
    vetor[n-e-1] = subs

print(f"Tamanho invertido do vetor: {vetor}")







