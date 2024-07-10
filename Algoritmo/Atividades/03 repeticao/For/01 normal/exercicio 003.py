#Faça um programa que calcule e mostre o fatorial de um número N, fornecido
# pelo usuário. A definição de fatorial é mostrada a seguir:

fatorial = int(input("Digite um valor: "))
multiplicador = 1
for contador in range(fatorial, 1, -1):
    multiplicador *= contador
print(f"{fatorial}! = {multiplicador}")