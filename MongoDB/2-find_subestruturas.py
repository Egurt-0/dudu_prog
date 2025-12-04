from  pymongo import MongoClient
from pprint import pprint
client = MongoClient()

db = client['nobel']

prizes = db['prizes']
laureates = db['laureates']

# importante lembrar que essa logica a baixo e bem simples, ela se resume a logica de dicionarios, voce da a chave, e em seguida o valor.


# buscando documento

Vitaly_L = db.laureates.find_one({ # esse find_one, retorna todos os valores, nao so a quantidade como os exemplos a baixo
                                    # nesse caso queria que ele retornasse tudo sobre esse Vitaly L.
    'firstname': 'Vitaly L.'
})

pprint(f"{Vitaly_L}\n") # usando o pprint para deixar mais formatado



# pesquisando em uma subestrutrura

california = db.laureates.count_documents({
    'prizes.affiliations.name': 'University of California' # aqui ele esta procurando no prizes e dentro de prizes nas affiliations e dentro delas a o name University of California
    # essa que e a procura nas subestruturas, voce vai trasando um caminho. nesse caso ele retorna quantos vencedores do premio nobel sao afiliados a universidade da california

})


print(f"Existem {california} premio nobeis afiliados a universidade da california\n")


Paris = db.laureates.count_documents({ # esse count_documentes vai me retornar so o valor numerico, ou seja, quantos existem, nao quais
    'prizes.affiliations.city': 'Paris'#  fazendo a mesma coisa de antes, mas agora com um path diferente. o retorno e parecido com o outro, mas agora ele retorna os vencedores do premio nobel
    # que tem afiliacao com a cidade de paris
})

print(f"Existem {Paris} premio nobeis afiliados a cidade de paris\n")


new_york = db.laureates.count_documents({
    'prizes.affiliations.city': 'New York, NY' # mesma coisa que o anterior.
})

print(f"Existem {new_york} premio nobeis afiliados a Nova iorque\n")



# verificando se os laureados possuem premio
qtd = db.laureates.count_documents({})
print(f"temos exatamente {qtd} laureados\n")

# isso e ridiculo, ele quer saber quantos laureados tem premio, sendo que para ser um laureado voce precisa ganhar um premio
quem_tem_premio = db.laureates.count_documents({
    "prizes": {
        '$exists': True
    }
})
print(f"Sao exatamente {quem_tem_premio} Laureados que tem premios\n")



# Verificacao se o prize esta preenchido 
prize_preenchido = db.laureates.count_documents({
    'prizes.0': {
        '$exists' : True
    }
})

print(f"seila, nao faz diferenca a esse ponto {prize_preenchido} isso aqui\n")


mais_de_um_premio = db.laureates.count_documents({
    'prizes.1': {
        '$exists' : True
    }
})

print(f"Exsitem {mais_de_um_premio} laureados com mais de um premio nobel\n")