from  pymongo import MongoClient


client = MongoClient()

db = client['nobel']

prizes = db['prizes']
laureates = db['laureates']


# como Contar documentos por genero
print(f"Existem atualmente {db.laureates.count_documents({'gender': 'female'})} mulheres que ganharam o premio nobel")
print(f"Existem atualmente {db.laureates.count_documents({'gender': 'male'})} homens que ganharam o premio nobel")

# contar documetos pela bron country

print(f"{db.laureates.count_documents({'bornCountry': 'Brazil'})} Brasileiro(s) ganhou o premio nobel")
print(f"{db.laureates.count_documents({'bornCountry': 'United Kingdom'})} Inlgeses ganharam o premio nobel")
print(f"{db.laureates.count_documents({'bornCountry': 'France'})} Franceses ganharam o premio nobel")



# contar documentos pela data de nascimento antes de 1950
print(f"Existem {db.laureates.count_documents({'born': {'$lt': '1920-01-01'}})} vencedores do premio nobel que nasceram antes de 1920")


filter_doc = {
    'bornCountryCode': 'GB', # United Kingdom
    'gender': 'male',
    'diedCountryCode': 'US'
}


print(f"Existem atualmente {db.laureates.count_documents(filter=filter_doc)} ganhadores do premio nobel que sao homens nasceram nos UK e  morreram nos US")