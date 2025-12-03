from  pymongo import MongoClient
from pprint import pprint
import timeit
client = MongoClient()
db = client['nobel']
prizes = db['prizes']
laureates = db['laureates']

# IMPORTANTE: esse arquivo aqui ele mostra bem a confusao que fica, com os () {} [] enfim, isso muda tudo, tem que tomar cuidado
# oque esta dentro de lista, oque esta dentro das chaves, virgulas, isso e um universo inteiro para dominar

# premio concedidos entre 1966 e 1977
for doc in db.prizes.find(
    {'year': {'$gt':'1966', '$lt':'1977'}},
    ['category', 'year'],
    sort=[('year', 1), ('category', 1)]):
    print('{year} {category}'.format(**doc))
    print("\n")



# todos os premios compartilhados entre 3 pessoas
for doc in db.prizes.find({'laureates.share': '3'}, sort=[('year', 1)], skip=5, limit=5): # o skip pula, kkkkk, nesse caso ele ignorou os 5 primeiros itens, e o limit so estabelece um limite para o print
    print('{year} {category}'.format(**doc))
    print("\n")


for doc in db.prizes.find({'laureates.share': '3'}) \
    .sort([('year', 1)]) \
    .skip(9) \
    .limit(14):
        print('{year} {category}'.format(**doc))
        print("\n")