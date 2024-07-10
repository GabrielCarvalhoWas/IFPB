# Exercicio 01

# A Companhia de Carros Usados João Honesto paga seus empregados um salário de R$
# 1.000,00 por mês mais uma comissão de R$ 200,00 por cada carro vendido mais 5% do
# valor da venda.
# Escreva um programa que leia o nome, o número de carros vendidos e o valor total das
# vendas de um vendedor, e calcule e exiba o seu salário.

nome = str(input("Digite o seu nome: "))
numeroCarroVendido = int(input("Digite quantos carros foi vendido: "))
valorTotal = float(input("Digite o valor total das vendas: "))
numeroCarroVendido *= 200
salario = 1000 + numeroCarroVendido + (valorTotal * 0.05)
print(f"Salário do vendedor: {salario:.2f}")