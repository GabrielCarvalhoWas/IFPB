# QUESTÃO 2
# Escreva um programa que faça 5 perguntas para uma pessoa sobre um crime. As # perguntas são:
# • "Telefonou para a vítima?"
# • "Esteve no local do crime?"
# • "Mora perto da vítima?"
# • "Devia para a vítima?"
# • "Já trabalhou com a vítima?"
# Todas as respostas devem ser apenas "S" (para "Sim") ou "N" (para "Não").
# O programa deve, no final, imprimir uma classificação sobre a participação da # pessoa no crime. Se
# a pessoa responder "S" a 2 perguntas ela deve ser classificada como "Suspeita", # entre 3 e 4 como
# "Cúmplice" e 5 como "Assassino". Caso contrário, ela será classificada como # "Inocente".
acumulador = 0
perguntas = 5
while perguntas > 0:
    pergunta1 = str(input("Telefonou para a vítima? [S/N]: ")).upper()
    if pergunta1 == "S":
        perguntas -= 1
        acumulador += 1
    else:
        if pergunta1 == "N":
            perguntas -= 1

    pergunta2 = str(input("Esteve no local do crime? [S/N]: ")).upper()
    if pergunta2 == "S":
        perguntas -= 1
        acumulador += 1
    else:
        if pergunta2 == "N":
            perguntas -= 1

    pergunta3 = str(input("Mora perto da vítima? [S/N]: ")).upper()
    if pergunta3 == "S":
        perguntas -= 1
        acumulador += 1
    else:
        if pergunta3 == "N":
            perguntas -= 1

    pergunta4 = str(input("Devia para a vítima? [S/N]: ")).upper()
    if pergunta4 == "S":
        perguntas -= 1
        acumulador += 1
    else:
        if pergunta4 == "N":
            perguntas -= 1

    pergunta5 = str(input("Já trabalhou com a vítima? [S/N]: ")).upper()
    if pergunta5 == "S":
        perguntas -= 1
        acumulador += 1
    else:
        if pergunta5 == "N":
            perguntas -= 1



if acumulador == 2:
    print("Suspeita")

elif acumulador == 3 or acumulador == 4:
    print("Cúmplice")
elif acumulador == 5:
    print("Assassino")
else:
    print("Inocente")




    

        
