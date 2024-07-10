# Escreva um programa que leia o nome e o sexo (M ou F) de uma pessoa e exiba a mensagem
# "Olá, Sr. Fulano!" ou "Olá, Sra. Fulana!", de acordo com o sexo da pessoa. Obs: Fulano e Fulana
# são nomes exemplos.

nome = str(input("Digite o nome: "))
sexo = str(input("Digite o sexo [M/F]: "))[0].upper()
if sexo == "M":
    print(f"Olá, Sr. {nome}!")
elif sexo == "F":
    print(f"Olá, Sra. {nome}!")
else:
    print("Erro, sexo inválido!")