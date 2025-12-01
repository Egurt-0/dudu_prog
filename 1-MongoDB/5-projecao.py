from  pymongo import MongoClient
from pprint import pprint
from bson.regex import Regex
client = MongoClient()


db = client['nobel']

prizes = db['prizes']
laureates = db['laureates']

# 1-valor incluido(projeta)
# 0-valor nao incluido(nao projeta)

docs = db.laureates.find(
    filter = {},
    projection = {
        'prizes.affiliations': 1,
        '_id':0
    }
)


#print(list(docs))
# nesse caso nao coloquei [:?] por isso ele retorna tudo
# esse comando retorna coisa para caralho print(list(docs))


pprint(f"3 affiliations chegando: {list(docs[:3])}") # esse [:2] e eu determinando quantos quero FIND, se eu nao uso ele, ele retorna tudo, mas se eu coloco, por exemplo:  [:4]  ele retorna so 4 prizes affiliations
# entao use esse aqui, caso queria deixar sua tela mais limpa


# projecao de campos ausentes
docs2 = db.laureates.find(
    filter = {'gender': 'female'},
    projection = ['bornCountry', 'firstname']
)
pprint(f" 3 vencedoras, pais e nome : {list(docs2[:3])}")