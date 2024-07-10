# Faça um programa que leia um número N, inteiro, e some todos os números
# de 1 até N, mostrando o resultado.
contador = 0
N = int(input("Digite um numero: "))
for somador in range(1, N + 1):
    contador += somador
print(f"resultado: {contador}")