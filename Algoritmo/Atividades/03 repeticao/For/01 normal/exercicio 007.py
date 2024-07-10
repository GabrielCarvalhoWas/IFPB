primo = int(input("Digite um numero: "))
acumulador = 0
for contador in range(2, primo):
    if primo % contador == 0:
        acumulador += 1
if acumulador == 0 and primo != 1:
    