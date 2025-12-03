from  pymongo import MongoClient
from pprint import pprint
client = MongoClient()
db = client['nobel']
prizes = db['prizes']
laureates = db['laureates']


# ordenacao ascendente
cursor = db.prizes.find(
    {'category': 'physics'},
    ['year', 'category'], # aqui estou definindo quais informacoes vou projetar, nesse caso o ano e a catogoria
    sort=[('year', 1)] # aqui e a ordenacao, uso o sort= depois uma lista, dentro da lista precisa colocar um tupla, digo com base no que vou ordernar, nesse caso o year, depois
    # uso 1 para ordenar ascendentemente ou -1 para desencente
)
# pprint(list(cursor)) # voce pode usar isso como forma para o print
print([doc['year'] for doc in cursor][:5]) # pode usar O LIST COMPREHENSION, que printa apenas os 5 primeiros anos



#4 premio concedidos entre 1966 e 1977
for doc in db.prizes.find(
    {'year': {'$gt':'1966', '$lt':'1977'}},
    ['category', 'year'],
    sort=[('year', 1), ('category', 1)]):
    print('{year} {category}'.format(**doc))



# LIST COMPREHENSION, exemplos

quadrados = [x**2 for x in range(6)]
print(quadrados)
# Resultado: [0, 1, 4, 9, 16, 25]
# ele nao vai ate o 6 porque comeca no 0


numeros = [1, 2, 3, 4, 5, 6]
pares = [n for n in numeros if n % 2 == 0]
print(pares)
# Resultado: [2, 4, 6]
exemplo_dudu = [y/100000000000 for y in range(10)] # ele retorna em notacao cientifica ate kkkkkkkkkk
print(exemplo_dudu)