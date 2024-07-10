# Faça um programa que leia os seguintes dados de um conjunto de alunos:
# matrícula, nome e as duas notas que ele obteve em suas avaliações. A
# condição de parada será a digitação de uma matrícula igual 0 (zero). O
# programa deverá mostrar, para cada aluno, as seguintes informações:
# matrícula, nome, média e situação (aprovado, se a média for igual ou superior
# a 7 e, reprovado, se a média for inferior a 7).


while True:
    matricula = int(input("Digite sua matricula: "))
    if matricula == 0:
        break
    nome = str(input("Digite seu nome: "))
    nota1 = float(input("Digite sua primeira nota: "))
    nota2 = float(input("Digite sua segunda nota: "))
    media = (nota1 + nota2) / 2
    if media >= 7:
        situacao = "aprovado"
    else:
        situacao = "reprovado"

    print(f"Matricula: {matricula}")
    print(f"Nome: {nome}")
    print(f"Media: {media}")
    print(f"Situacao: {situacao}")

