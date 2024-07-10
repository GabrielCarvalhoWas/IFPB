# Exercicio 007
# O restaurante a quilo Bem-Bão cobra R$25,00 por cada quilo de refeição. Faça um
# programa que leia o peso do prato montado pelo cliente (em quilos) e exiba o valor
# a pagar. Assuma que a balança já desconte o peso do prato.
peso = float(input("Peso do prato: "))
pagar = peso * 25
print(f"Preço a pagar: {pagar:.2f}")