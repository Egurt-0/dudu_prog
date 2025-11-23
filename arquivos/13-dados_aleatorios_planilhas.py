import pandas as pd
import numpy as np


dados_aba1 = {
    "ID" : [1, 2, 3, 4, 5],
    "Nome" : ["Ana Alice", "guimaraes", "sabado", "gorilas", "Maicon Jackson"],
    "Idade" : [ 23, 25, 46, 25, 62],
    "Cidade" : ["Curitiba", "Porto Alegre", "Sao paulo", "States", "Nomade"]

}


dados_aba2 = {
    "ID" : [25, 672, 732, 727, 767],
    "Nome" : ["Alice", "guilherme", "Theo filho da puta", "Gorilazz", "Coco na privada"],
    "Idade" : [ 32, 73, 27, 85, 52],
    "Cidade" : ["Curitiba", "Sao paulo", "Sao paulo", "Porto Alegre", "Nomade"]
    
}

dados_aba3 = {
    "ID" : [692, 53203, 583, 723357, 4327],
    "Nome" : ["Lauro", "Fagundes", "Theo filho da puta", "Duduuu", "Lavanda"],
    "Idade" : [ 54, 89, 11, 71, 62],
    "Cidade" : ["Curitiba", "Curitba", "MADRID", "Curitiba", "Aqui"]
    
}

dados_aba4 = {
    "ID": [76023, 23863, 96382, 0000, 7832],
    "Nome": ["Lucas Pereira", "Maria Costa", "João Victor", "Helena Souza", "Gabriel Lima"],
    "Idade": [19, 30, 27, 21, 34],
    "Cidade": ["Curitiba", "Rio de Janeiro", "São Paulo", "Belo Horizonte", "Florianópolis"]
}


df_aba1 = pd.DataFrame(dados_aba1)
df_aba2 = pd.DataFrame(dados_aba2)
df_aba3 = pd.DataFrame(dados_aba3)
df_aba4 = pd.DataFrame(dados_aba4)


caminho_arquivo = "dados/clientes.xlsx"

with pd.ExcelWriter(caminho_arquivo, engine="openpyxl") as writer:
    df_aba1.to_excel(writer, sheet_name="Aba1", index=False)
    df_aba2.to_excel(writer, sheet_name="Aba2", index=False)
    df_aba3.to_excel(writer, sheet_name="Aba3", index=False)
    df_aba4.to_excel(writer, sheet_name="Aba4", index=False)


print(f"Arquivo excel com 4 abas criadas em {caminho_arquivo}")