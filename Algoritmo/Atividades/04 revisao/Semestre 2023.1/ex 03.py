# QUESTÃO 3
# A prefeitura de uma cidade fez uma pesquisa com várias pessoas coletando dados sobre a idade e
# o salário de cada uma delas.
# Escreva um programa que leia esses dados acima, calcule e imprima:
# • A média de idade;
# • O menor salário;
# • A quantidade de pessoas com idade de 18 anos e salários até R$ 1.500,00.
# Obs: a leitura da idade 0 (zero) indicará o final dos dados de entrada.


idade = Menorsalario = acumulador = pobre = 0
acumulador2 = 1
while idade >= 0:
    idade = int(input("Digite sua idade: "))
    if idade == 0:
        break
    salario = float(input("Digite o seu salario: "))
    Menorsalario = salario
    if salario < Menorsalario:
        Menorsalario = salario
        
    acumulador += idade
    acumulador2 += 1
    if idade == 18 and salario <= 1500:
        pobre += 1
    
print(f"Media das idades: {acumulador/(acumulador2-1):.0f} anos.")
print(f"Menor salario: R$ {Menorsalario}.")
print(f"Temos {pobre} pessoas com 18 anos e com salários até R$ 1.500,00.")

    

