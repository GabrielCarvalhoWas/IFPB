# Escreva um programa que leia um vetor contendo N elementos inteiros (N será
# lido), calcule e exiba:
# • A quantidade de elementos pares;
# • A quantidade de elementos ímpares;
# • A soma de todos os elementos;
# • A média dos elementos do vetor.

n = int(input("Digite o tamanho do vetor: "))

vetor = [0] * n
pares = impares = somaElementos = 0

for i in range(n):
    vetor[i] = int(input(f"Digite o {i+1} elemento: "))
    somaElementos += vetor[i]
    
    if vetor[i] % 2 == 0:
        pares +=1
    else:
        impares += 1


media = somaElementos / n

print(f"Quantidade de elementos pares: {pares}")
print(f"Quantidade de elementos impares: {impares}")
print(f"Soma de todos os elementos: {somaElementos}")
print(f"Media dos elementos do vetor: {media}")



