# Faça um programa que leia 3 números inteiros (N, X, Y) e mostre todos os
# números múltiplos de N entre X e Y.
N = int(input("Digite um valor: "))
X = int(input("Digite outro valor: "))
Y = int(input("Digite outro valor: "))
print(f"Os multiplos de N entre X e Y são:", end=' ')
for contador in range(X, Y+1):
    if contador % N == 0:
        print(contador, end=' ')
        