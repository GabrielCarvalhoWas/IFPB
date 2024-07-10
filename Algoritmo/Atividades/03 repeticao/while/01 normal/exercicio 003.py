# Faça um programa que leia vários números, determine e mostre o maior e o
# menor deles.
# Obs: a leitura do número 0 (zero) encerra o programa.
encerracao = 0
leitura = int(input("Digite algo: "))
maior = leitura
menor = leitura
while leitura != encerracao:
    if leitura > maior:
        maior = leitura
    if leitura < menor:
        menor = leitura
    leitura = int(input("Digite algo: "))
print(f"Maior numero: {maior}")
print(f"Menor numero: {menor}")
        
