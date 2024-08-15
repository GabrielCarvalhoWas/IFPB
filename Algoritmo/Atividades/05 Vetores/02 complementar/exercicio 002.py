# Dados dois vetores A e B contendo N elementos inteiros cada (N, A e B serão
# lidos), gerar e exibir um vetor C (de tamanho N*2) cujos elementos sejam a
# intercalação dos elementos de A e B.
# Ex: N = 3, A = [18, 12, 20], B = [15, 10, 7], C = [18, 15, 12, 10, 20, 7]

n = int(input())
vetor_A = [0] * n
for i in range(n):
    vetor_A[i] = int(input())

vetor_B = [0] * n
for i in range(n):
    vetor_B[i] = int(input())


vetor_C = [0] * (n*2)

for i in range(n):
    vetor_C[i*2] = vetor_A[i]
    vetor_C[i*2+1] = vetor_B[i]


print(vetor_A)
print(vetor_B)
print(vetor_C)