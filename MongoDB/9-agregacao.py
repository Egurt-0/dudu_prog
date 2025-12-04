from  pymongo import MongoClient
from pprint import pprint
import timeit
client = MongoClient()
db = client['nobel']
prizes = db['prizes']
laureates = db['laureates']


cursor = db.laureates.find({'bornCountry': 'USA'}, {'prizes.year': 1, '_id': 0}, limit=5)
for doc in cursor:
    print(doc)
print("\n")


conta = db.laureates.count_documents({}) # esse comando no mongo, de coun_documents, find, find_one, tudo, precisa de um filtro {?},
# mas se eu nao quiser filtrar, apenas deixo o filtro vazio {}, mas ainda preciso colocar ele
print(f"Numero total de laureados: {conta}\n")



# refatorando cosulta com agreagacoes
cursor1 = db.laureates.aggregate([
    {'$match': {'bornCountry': 'USA'}},
    {'$project': {'prizes.year': 1}},
    {'$limit': 3}
])

for doc in cursor:
    print(doc)
    print("\n")


# adicionando novas etapas na agregacao
from collections import OrderedDict
cursor2 = db.laureates.aggregate([
    {'$match': {'bornCountry': 'USA'}},
    {'$project': {'prizes.year': 1, '_id': 0}},
    {'$sort': OrderedDict([('prizes.year', 1)])},
    {'$limit': 3}
])
for doc in cursor2:
    print(doc)



# quantos laureados nasceram nos EUA
cursor3 = db.laureates.aggregate([
    {'$match': {'bornCountry': 'USA'}},
    {'$count': 'quantos_nasceram_nos_EUA'}
])
print(list(cursor3))
print("\n")