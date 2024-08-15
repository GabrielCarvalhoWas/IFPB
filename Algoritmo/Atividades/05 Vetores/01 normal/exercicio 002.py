# Escreva um programa que leia um vetor V (contendo 30 inteiros) e um valor
# inteiro K, calcule e exiba a quantidade de ocorrências de K dentro de V.
V = [0] * 30
k = int(input("Digite: "))
for i in range(len(V)):
    V[i] = V[i] * k

print(V)