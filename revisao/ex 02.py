cliente = float(input("Digite o valor da compra: "))
if cliente < 30:
    print("sem cupons")
    print(f"R$ {cliente:.2f} de saldo")
    print(f"R$ {30 - cliente:.2f} para novo cupom")
else:
    cliente02 = cliente // 30
    print(f"{cliente02:.0f} cupons")
    print(f"R$ {cliente % 30:.2f} de saldo")
    print(f"R$ {30- (cliente % 30):.2f} para novo cupom")
