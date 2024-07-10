# Escreva um programa que leia o peso (kg) e a altura (m) de uma pessoa, determine e mostre o
# seu grau de obesidade, de acordo com a tabela seguinte. O grau de obesidade é determinado
# pelo índice de massa corpórea, cujo cálculo é realizado dividindo-se o peso da pessoa pelo
# quadrado da sua altura.

# Valor do IMC Grau de Obesidade
# < 18,5 Baixo peso
# ≥ 18,5 e < 25 Normal
# ≥ 25 e < 30 Sobrepeso
# ≥ 30 Obesidade


peso = float(input("Digite o seu peso: "))
altura = float(input("Digit sua altura: "))
imc = peso / (altura * altura)
if imc < 18.5:
    print("Baixo peso")
elif imc >= 18.5 and imc < 25:
    print("Normal")
elif imc >= 25 and imc < 30:
    print("Sobrepeso")
else:
    print("Obesidade")