# Escreva um programa que tenha a funcionalidade de uma calculadora simples. O programa deve
# solicitar a digitação de dois operandos e um operador (+ - x * / %) e deve imprimir ao resultado
# da operação aritmética. Caso o usuário digite um operador inválido, o programa deve imprimir  "Operador desconhecido".

operando01 = int(input("Digite um valor: "))
operando02 = int(input("Digite outro valor: "))
operador = str(input("Digite um operador: [+ - x * / %]: ")).lower()
if operador == "+":
    adicao = operando01 + operando02
    print(f"{operando01} {operador} {operando02} = {adicao}")
elif operador == "-":
    subtracao = operando01 - operando02
    print(f"{operando01} {operador} {operando02} = {subtracao}")
elif operador == "x":
    multiplicacao = operando01 * operando02
    print(f"{operando01} {operador} {operando02} = {multiplicacao}")
elif operador == "*":
    potencia = operando01 ** operando02
    print(f"{operando01} {operador}{operador} {operando02} = {potencia}")
elif operador == "/" or operador == "//":
    divisao = operando01 / operando02
    print(f"{operando01} {operador} {operando02} = {divisao}")
elif operador == "%":
    resto = operando01 % operando02
    print(f"{operando01} {operador} {operando02} = {resto}")
else:
    print("Operador desconhecido.")








