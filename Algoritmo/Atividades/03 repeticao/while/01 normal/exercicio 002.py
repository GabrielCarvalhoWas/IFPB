# Faça um programa que leia vários números, calcule e exiba a média desses
# números.
# Obs: a leitura do número 999 indica o fim dos dados de entrada e não deve ser
# computado na média)
somador = contador = 0
while True:
    numero = int(input("Digite um valor: "))
    if numero == 999:
        break
    else: 
        somador += numero
        contador += 1
media = somador / contador
print(f"Media desses números: {media:.2f}")

