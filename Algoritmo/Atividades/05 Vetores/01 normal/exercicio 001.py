# 1. Escreva um programa que leia um vetor A de N números inteiros (N será lido) e
# um outro inteiro K, construa e exiba um outro vetor B cujos elementos são os
# respectivos elementos de a multiplicados por K.
# Ex: A = [1,2,3], K = 5, B = [5,10,15].

n = int(input("N: "))
vetor_A = [0] * n
vetor_B =[]

for i in range(n):
    vetor_A[i] = int(input(f"Elemento {i+1}: "))
k = int(input("K: "))

vetor_B = [0] * n
for i in range(n):
    vetor_B[i] = vetor_A[i] * k

print(vetor_A)
print(vetor_B)