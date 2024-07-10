#Escreva um programa que imprima a tabuada de um valor lido (de 1 a 10). Por exemplo, se for lido
# o valor 5, a saída deverá seguir o modelo abaixo:
# 1 x 5 = 5
# 2 x 5 = 10
# 3 x 5 = 15
# ...
# 10 x 5 = 50
# Obs: use a estrutura for.

tabuda = int(input("Digite um valor: "))
for contador in range(1,11):
    print(f"{contador} x {tabuda} = {contador * tabuda}")