import pandas
import pandas
import os
from pathlib import Path

# pegando todas as abas de uma vez só, e criando um dicionário com elas
tb_clientes_dict = pandas.read_excel("dados/clientes.xlsx", sheet_name=None)
print(type(tb_clientes_dict))

# criando uma pasta 'planilhas separadas' se nao existir
pasta_saida = "dados/planilhas_separadas"
if not os.path.exists(pasta_saida):
    os.makedirs(pasta_saida)

for nome_aba, tabela in tb_clientes_dict.items():
    caminho_arquivo = os.path.join(pasta_saida, f"{nome_aba}.xlsx")
    tabela.to_excel(caminho_arquivo, sheet_name=nome_aba, index=False)

# criando tabela de 'planilhas_consolidadas' se nao existir
pasta_consolidada = "dados/planilhas_consolidadas"
if not os.path.exists(pasta_consolidada):
    os.makedirs(pasta_consolidada)

# caminho para o arquivo
caminho_arquivo_consolidado = os.path.join(pasta_consolidada, "clientes.xlsx")

# consolidar planilhas (CORRIGIDO: engine="openpyxl")
with pandas.ExcelWriter(caminho_arquivo_consolidado, engine="openpyxl") as consolidada:
    for arquivo in Path(pasta_saida).glob("*.xlsx"):
        tabela = pandas.read_excel(arquivo)
        tabela.to_excel(consolidada, sheet_name=arquivo.stem, index=False)
