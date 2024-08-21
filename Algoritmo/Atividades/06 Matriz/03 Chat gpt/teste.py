import os


num_arquivos = 1

prefixo = "exercicio "

extensao = ".py"


for i in range(1, num_arquivos + 1):
    nome_arquivo = f"{prefixo}{i:03d}{extensao}"
    with open(nome_arquivo, 'w') as arquivo:
        arquivo.write(
"""# 
#""")
    print(f"Arquivo criado: {nome_arquivo}")