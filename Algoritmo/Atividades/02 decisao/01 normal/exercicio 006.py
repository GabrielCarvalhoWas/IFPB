# Recomendam-se estudantes para bolsas de estudo em função de seu desempenho.
# A natureza das recomendações é baseada na seguinte tabela:

# A = altamente recomendado 
# B  ou C = Recomendado
# D = Não recomendado

# Escreva um programa que leia o nome e o conceito de um estudante e exiba o nome do
# estudante e sua respectiva recomendação.

nome = str(input("Digite o seu nome: "))
conceito = str(input("Digite seu conceito: ")).upper()

if conceito == "A":
    print(f"Aluno: {nome}. Status: Altamente recomendado")
elif conceito == "B" or conceito == "C":
    print(f"Aluno: {nome}. Status: Recomendado.")
else:
    print(f"Aluno {nome}. Status: Não recomendado")


