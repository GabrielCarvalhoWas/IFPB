totalValor = 0
quantidadeCupons = 0
maiorValorVendido = 0
cuponsEntregue = 0
quantidadeCliente = 0
quantidadeCuponsNaoDistribuido = 1000

while quantidadeCuponsNaoDistribuido > 0:
        cliente = float(input("Digite o valor da venda: "))
        totalValor += cliente
        if cliente < 30:
            print("sem cupons.")
            print(f"R$ {cliente:.2f} de saldo.")
            print(f"R$ {30 - cliente:.2f} para novo cupom. ")
        else:
            cupons = cliente // 30
            quantidadeCupons += cupons
            saldo =  cliente % 30
            print(f"{cupons:.2f} cupons")
            print(f"{saldo:.2f} de saldo.")
            print(f"{(30 - saldo):.2f} para novo cupom.")
            if cliente > maiorValorVendido:
                maiorValorVendido = cliente
                cuponsEntregue = maiorValorVendido // 30

            if saldo == 0:
                quantidadeCliente += 1
            


print(f"Total do valor vendido no dia: {totalValor}.")
print(f"Quantidade de cupons distribuido nesse dia: {quantidadeCupons}.")
print(f"Maior valor vendido: {maiorValorVendido}.")
print(f"quantidade entregue: {cuponsEntregue}.")
print(f"Quantidade de clientes que receberam todos os cupons da sua compra: {quantidadeCliente}.")
print(f"Quantidade de cupons não distribuídos: {quantidadeCuponsNaoDistribuido}. ")


