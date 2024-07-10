# Faça um programa que calcule e mostre os números múltiplos de 5 do
# intervalo 50 a 300, juntamente com suas raízes e seus cubos.

print(f"Os números múltiplos são:", end=' ')
for multiplo in range(50, 301):
    if multiplo % 5 == 0:
        raiz = multiplo ** (1/2)
        cubico = multiplo ** 3
        print(f"{multiplo:5}, {raiz:10.4f} {cubico:10} ")
