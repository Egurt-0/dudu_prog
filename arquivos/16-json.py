import json



dados = {
    "clientes": [
            {"ID": 1, "Nome": "Ana", "Idade": 23, "Cidade": "Sao paulo"},
            {"ID": 2, "Nome": "Carlinhos maia", "Idade": 51, "Cidade": "Bocaiuva do Sul"},
            {"ID": 3, "Nome": "Frozen da era do gelo", "Idade": 21, "Cidade": "Era do gelo"}
        ]
}


caminho_aqruivo = "dados/clientes.json"

# escrevendo dados em json

with open(caminho_aqruivo, "w", encoding="utf-8") as f:
    json.dump(dados, f, indent=4)

# lendo os dados do arquivo json

with open("dados/clientes.json", "r", encoding="utf-8") as f:
    dados_lidos = json.load(f)
    print(dados_lidos)



# manipular os dados
for cliente in dados_lidos["clientes"]:
    if cliente["Nome"] == "Ana":
        cliente["Idade"] = 31



# novo cliente
novo_cliente = {"ID": 4, "Nome": "Xandeco", "Idade": 15, "Cidade": "Piraquara"}
dados_lidos["clientes"].append(novo_cliente)


# salvar os dados manipulados
with open("dados/clientes.json", "w", encoding="utf-8") as f:
    json.dump(dados_lidos, f, indent=4)



print("rodou tudo certinho aqui meu nobre, pode ficar despreocupado")