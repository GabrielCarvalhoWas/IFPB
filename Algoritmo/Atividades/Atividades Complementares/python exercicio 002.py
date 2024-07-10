# Exercicio 002

# Escreva um programa para calcular e exibir a média ponderada de 2 notas dadas. Sabe-
# se que nota1 possui peso 6 e nota2 possui peso 4.
peso1 = 6
peso2 = 4
nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))
mediaPonderada = ((nota1 * peso1) + (nota2 * peso2)) / 10
print(f"Media das notas: {mediaPonderada:.2f}")