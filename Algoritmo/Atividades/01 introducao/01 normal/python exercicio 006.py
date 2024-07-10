# Exercicios 06 
# Faça um programa que efetue a apresentação do valor da conversão em real (R$)
# de um valor lido em dólar (US$). O algoritmo deverá solicitar o valor da cotação do
# dólar e também a quantidade de dólares disponíveis com o usuário.
dolar = float(input("Digite o valor do dólar: U$ "))
usuario = float(input("Digite a quantidade de dolares que você tem disponivel: "))
conversao = usuario * dolar
print(f"Usuário tem no total R$ {conversao:.2f}.")


