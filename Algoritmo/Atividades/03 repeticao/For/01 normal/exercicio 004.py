# Faça um programa que leia 20 números inteiros, determine e mostre o maior
# deles.
maior = 0
for contador in range(20):
    valor = int(input("Digite um valor: "))
    if valor > maior:
        maior = valor
print(f"Maior valor encontrado: {maior}")