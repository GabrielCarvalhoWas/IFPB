# Exercicio 011
# Escreva um programa que leia 3 números inteiros, determine e mostre o maior deles. 
num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))
num3 = int(input("Digite o terceiro numero: "))

if num1 == num2 == num3:
    print("Todos os valores são iguais.")
elif num1 > num2 and num1 > num3:
    print(f"O primeiro valor: {num1} é o maior valor.")
elif num2 > num1 and num2 > num3:
    print(f"O segundo valor: {num2} é o maior valor.")
else:
    print(f"O terceiro valor: {num3} é o maior valor.")