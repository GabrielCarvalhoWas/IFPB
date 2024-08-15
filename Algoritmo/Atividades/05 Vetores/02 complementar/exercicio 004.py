# Escreva um programa para ler 6 números distintos, ou seja, não podem repetir.
# Exiba os números lidos.



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




