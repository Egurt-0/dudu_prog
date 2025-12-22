from random import *

# Dicionario de paises
paises = {
    "BR": "Brasil",
    "EUA": "Estados Unidos",
    "BL": "Belize",
    "PTR": "Porto Rico",
    "PT": "Portugal",
    "HT": "Haiti",
    "JM": "Jamaica"
}


paises_simbolo = []

for pais in paises.keys(): # pegando a chave da cada item do dicionario
    paises_simbolo.append(pais.lower()) # e adicionando (em minusculo) na lista paises_simbolo

print(paises_simbolo)


def dados_pais():
    index_aleatorio = randrange(0, len(paises_simbolo))
    imagem = "img/{}.{}".format(paises_simbolo[index_aleatorio], "png")
    key = paises_simbolo[index_aleatorio].upper()
    pais_nome = paises[key]

    return [imagem, pais_nome]