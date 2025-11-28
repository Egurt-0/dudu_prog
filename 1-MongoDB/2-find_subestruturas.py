from  pymongo import MongoClient
from pprint import pprint
client = MongoClient()

db = client['nobel']

prizes = db['prizes']
laureates = db['laureates']


# buscando documento

Vitaly_L = db.laureates.find_one({
    'firstname': 'Vitaly L.'
})

pprint(Vitaly_L)



# pesquisando em uma subestrutrura

california = db.laureates.count_documents({
    'prizes.affiliations.name': 'University of California'
})


pprint(f"Existem {california} premio nobeis afiliados a universidade da california")


Paris = db.laureates.count_documents({
    'prizes.affiliations.city': 'Paris'
})

pprint(f"Existem {Paris} premio nobeis afiliados a cidade de paris")


new_york = db.laureates.count_documents({
    'prizes.affiliations.city': 'New York, NY'
})

pprint(f"Existem {new_york} premio nobeis afiliados a Nova iorque")
