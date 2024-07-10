# Exercicio 008
# Faça um programa que leia o nome de um aluno e as notas das três provas que ele
# obteve no semestre. No final informar o nome do aluno e a sua média (aritmética).
nome = str(input("Digite o seu nome: "))
nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))
nota3 = float(input("Digite sua terceira nota: "))
media = (nota1 + nota2 + nota3) / 3
print(f"Nome do aluno: {nome}, sua media: {media:.2f}")