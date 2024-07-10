# Faça um programa que leia 30 números inteiros, calcule e mostre a soma deles
# Obs: não use o comando for, use while.
contador = somador = 0
while contador < 5:
    numero = int(input("Digite um valor: "))
    somador += numero
    contador += 1
print(f"Soma de todos os numeros: {somador}")

