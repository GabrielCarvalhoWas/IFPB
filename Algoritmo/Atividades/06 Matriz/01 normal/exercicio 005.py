# Escreva um programa que:
# • Crie uma matriz de ordem 20 x 4 e armazene nela as 3 notas dos 20 alunos de uma
# turma e a média de cada um deles.
# o As notas serão lidas e armazenadas nas 3 primeiras colunas da matriz;
# o As médias serão calculadas e armazenadas na 4a coluna da matriz.
# • Imprima as notas dos alunos e suas respectivas médias (no formato de matriz).
# • Calcule e imprima a média geral da turma.
# • Calcule e imprima o número de alunos com média superior à média geral da turma.




matriz = []

for i in range(3):
    linha = []
    somador = 0
    for j in range(3):
        nota = float(input())
        linha.append(nota)
    media = somador / 3
    linha.append(media)
    matriz.append(linha)


somadorMedia = somadorAcima = 0

for i in range(20):
    somadorMedia += matriz[i][3]

media02 = somadorMedia / 20



for i in range(20):
    if matriz[i][3] > media:
        somadorAcima += 1

for i in range(20):
    print("Nota: ", matriz[i][:3],", Media: ", matriz[i][3])


print()

print("Media da turma: ", media02)

print("Media das quantidade de alunos acima da media: ", somadorAcima)







