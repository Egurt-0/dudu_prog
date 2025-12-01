from  pymongo import MongoClient
from pprint import pprint
import timeit

client = MongoClient()
db = client['nobel']
prizes = db['prizes']
laureates = db['laureates']


# busca premios de 2010
def prizes_2010():
    list(db.prizes.find({'year': '2010'}))

# medir o tempo de execucao
def measures_execution_time(func):
    execution_time = timeit.timeit(func, globals=globals(),number=1) * 1000
    print(f"tempo de execucao da funcao {func} foi de : {execution_time:.2f} milissegundos")

# executando sem o indice
measures_execution_time('prizes_2010()')

# com o indice
db.prizes.create_index([('year, 1')])
measures_execution_time('prizes_2010()')

# 4 criando indice composto
db.prizes.create_index([('category', 1), ('year', 1)])

def economy_prizes():
    list(db.prizes.find(
        {'category': 'economics'},
        {'year': 1, '_id': 0}
    ))

measures_execution_time('economy_prizes()')