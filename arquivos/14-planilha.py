import pandas as pd
import numpy as np


# 1 importando dados
tb_clientes = pd.read_excel("dados/clientes.xlsx", sheet_name="Aba2")
print(tb_clientes)
print(type(tb_clientes))

# 2 adiconando coluna de index

tb_clientes = pd.read_excel("dados/clientes.xlsx", index_col=0)
print(tb_clientes)

# 3 importar colunas especificas
tb_clientes = pd.read_excel("dados/clientes.xlsx", usecols=[0,1])
print(tb_clientes)

# 4 importar dados na planilha, pegar apenas a Aba1 e a Aba2 e criar outro arquivo apenas com essa duas abas
tb_clientes_aba1 = pd.read_excel("dados/clientes.xlsx", sheet_name= "Aba1")
tb_clientes_aba2 = pd.read_excel("dados/clientes.xlsx", sheet_name= "Aba2")

with pd.ExcelWriter("dados/novos_clientes.xlsx") as nova_planilha:
    tb_clientes_aba1.to_excel(nova_planilha, sheet_name="Aba1", index=False)
    tb_clientes_aba2.to_excel(nova_planilha, sheet_name="Aba2", index=False)


