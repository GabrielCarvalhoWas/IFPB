# Faça um programa que, para um grupo de N pessoas (obs: N será lido):
# • Leia o sexo (M ou F) de cada pessoa;
# • Calcule e escreva o percentual de homens;
# • Calcule e escreva o percentual de mulheres.

grupo = int(input("Digite uma quantidade: "))
masculino = feminino = 0
for contador in range(grupo):
    sexo = str(input("Digite o sexo [M/F]: ")).upper()
    if sexo == "M":
        masculino += 1
    elif sexo == "F":
        feminino += 1
    else:
        print("Erro.")
print(f"Percentual de homens: {(masculino * 100)/grupo:.2f} %.")
print(f"Percentual de mulheres: {(feminino * 100)/ grupo:.2f} %.")


