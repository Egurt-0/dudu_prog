from  pymongo import MongoClient
from pprint import pprint
client = MongoClient()

db = client['nobel']

prizes = db['prizes']
laureates = db['laureates']


print(db.laureates.distinct('gender\n'))


orgs = db.laureates.count_documents({'gender': 'org'})
exemplo_de_org = db.laureates.find_one({'gender': 'org'})
categorys = db.prizes.distinct('category')

chemistry = db.prizes.count_documents({'category': 'chemistry'})
economics = db.prizes.count_documents({'category': 'economics'})
literature = db.prizes.count_documents({'category': 'literature'})
medicine = db.prizes.count_documents({'category': 'medicine'})
physics = db.prizes.count_documents({'category': 'physics'})
peace = db.prizes.count_documents({'category': 'peace'})





print(f"existem {orgs} organizacoes que ganharam o premio nobel\n")
print(f"categorias: {categorys}\n")

print(f"Existem {chemistry} premio nobeis of chemistry\n")
print(f"Existem {economics} premio nobeis of economics\n")
print(f"Existem {literature} premio nobeis of literature\n")
print(f"Existem {medicine} premio nobeis of medicine\n")
print(f"Existem {physics} premio nobeis of physics\n")
print(f"Existem {peace} premio nobeis of peace\n")
