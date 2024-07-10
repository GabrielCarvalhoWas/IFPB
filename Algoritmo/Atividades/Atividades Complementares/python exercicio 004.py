# Exercicio 004

# Um motorista anota a marcação do hodômetro do seu veículo antes e após uma viagem,
# bem como o número de litros de combustível gastos.
# Escreva um programa que leia os 3 dados acima, o preço do litro de combustível, a
# capacidade do tanque e mostre:
# a) Quilometragem rodada.
# b) Quantos quilômetros por litro faz o veículo.
# c) Autonomia do veículo.
# d) Custo da viagem.


antesHodometro = float(input("Antes do hodometro: "))
depoisHodometro = float(input("Depois do hodometro: "))
litrosCombustivelGastos = float(input("Litros gastos: "))
precoCombustivel = float(input("Digite o preço do combustivel: R$ "))
capacidadeTanque = int(input("Digite a capacidade do tanque: "))

quilomentragemRodado = depoisHodometro - antesHodometro


quilometroPorLitro =  quilomentragemRodado / litrosCombustivelGastos 


autonomiaVeiculo = capacidadeTanque * quilometroPorLitro



custoViagem = quilomentragemRodado * precoCombustivel


print(f"Quilomentragem Rodado: {quilomentragemRodado}.")
print(f"Litro por KM: R$ {quilometroPorLitro}. ")
print(f"Autonomia do veiculo: {autonomiaVeiculo} KM.")
print(f"Custo da viagem: {custoViagem}")





#Autonomia do Veículo: Para calcular a autonomia do veículo, você multiplica a capacidade máxima do tanque pela eficiência, que é quantos quilômetros ele faz por litro. A fórmula correta seria capacidadeTanque * quilometroPorLitro.

#Custo da Viagem: Para calcular o custo da viagem, você multiplica o total de litros gastos pelo preço do combustível. A fórmula correta seria litrosCombustivelGastos * precoCombustivel.

#Hodômetro: Para calcular a quilometragem rodada, você subtrai o valor do hodômetro depois da viagem pelo valor do hodômetro antes da viagem. A fórmula correta seria depoisHodometro - antesHodometro.

#Quantidade de Litros por Quilômetro: Para calcular quantos litros o veículo faz por quilômetro, você divide a quantidade de total de quilômetros rodados litros gastos pelo. A fórmula correta seria quilomentragemRodado / litrosCombustivelGastos.