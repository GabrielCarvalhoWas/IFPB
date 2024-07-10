#A empresa Vende Tudo Ltda paga o salário de cada vendedor com uma comissão de 5% sobre o

#total de vendas daquele vendedor, mas essa comissão nunca deve ser inferior ao salário-
#mínimo. Escreva um programa que leia o valor total das vendas de um vendedor e escreva seu salário.

salarioMinimo = float(input("Digite o salario minimo: "))
vendaTotal = float(input("Digite o valor total da sua venda: "))
comissao = vendaTotal * 0.05
if comissao < salarioMinimo:
    salario = salarioMinimo
else:
    salario = comissao

print(f"Salario do vendedor foi de R$ {salario:.2f}")
