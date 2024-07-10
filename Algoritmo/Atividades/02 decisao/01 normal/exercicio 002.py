# Exercicio 010
# Escreva um programa que leia dois números e exiba-os em ordem crescente.
numero1 = float(input("Digite um número: "))
numero2 = float(input("Digite outro número: "))
print()
if numero1 > numero2:
    print(f"{numero1:.2f}")
    print(f"{numero2:.2f}")
else:
    print(f"{numero2:.2f}")
    print(f"{numero1:.2f}")