# Escreva um programa que leia um vetor V contendo N elementos inteiros (N será
# lido) e um valor inteiro K, verifique e exiba se o K está ou não no vetor. Se estiver,
# informe em que posição (índice).
# Obs: K pode se repetir no vetor, nesse caso, mostre todas as posições onde o K
# aparece.
n = int(input())
vetor = [0] * n

for i in range(n):
    vetor[i] = int(input())
    
k = int(input())
encontrado = False
for e in range(n):
     if vetor[e] == k:
        print(f"O valor de {k} está na posição {e}")
        encontrado = True

if not encontrado: 
    print(f"O item {k} não foi encontrado no vetor")