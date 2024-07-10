totalValor = 0
quantidadeCupons = 0
maiorValorVendido = 0
cuponsEntregue = 0
for vendas in range(3):
    cliente = float(input("Digite o valor da venda: "))
    totalValor += cliente
    if cliente < 30:
        print("sem cupons.")
        print(f"R$ {cliente:.2f} de saldo.")
        print(f"R$ {30 - cliente:.2f} para novo cupom. ")
    else:
        cupons = cliente // 30
        quantidadeCupons += cupons
        print(f"{cupons:.2f} cupons")
        print(f"{cliente % 30:.2f} de saldo.")
        print(f"{30 - (cliente % 30):.2f} para novo cupom.")
        if cliente > maiorValorVendido:
            maiorValorVendido = cliente
            cuponsEntregue = maiorValorVendido // 30
print(f"Total do valor vendido no dia: {totalValor}.")
print(f"Quantidade de cupons distribuido nesse dia: {quantidadeCupons}.")
print(f"Maior valor vendido: {maiorValorVendido}.")
print(f"quantidade entregue: {cuponsEntregue}.")
