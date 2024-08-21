# Uma empresa está com uma promoção relâmpago! Para cada R$ 30,00 (trinta reais) em
# compras o cliente receberá 01 (um) cupom. Escreva um programa para ler o valor da
# compra de um cliente e exiba:
# ● Quantidade de cupons que ele vai receber;

# ENTRADA SAÍDA

# 120.00 4 cupons
# 320.00 10 cupons
# 29.99 0 cupons

n = float(input())
cupom = n // 30
print(f"{cupom:.0f} cupons")