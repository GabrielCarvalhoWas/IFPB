# Escreva um programa para ler 6 números. Após a leitura dos números, verifique,
# para cada um deles, se é distinto, ou seja, não possui repetição.

n = 6
contador = 0
vetor = []
while contador < n:
    number = int(input())
    if number in vetor:
        print("Esse numero ja foi inserido")
    else:
        vetor.append(number)
        contador += 1

print(vetor)




