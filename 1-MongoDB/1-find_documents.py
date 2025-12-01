from  pymongo import MongoClient


client = MongoClient()

db = client['nobel']

prizes = db['prizes']
laureates = db['laureates']


# como Contar documentos por genero
print(f"Existem atualmente {db.laureates.count_documents({'gender': 'female'})} mulheres que ganharam o premio nobel\n")
print(f"Existem atualmente {db.laureates.count_documents({'gender': 'male'})} homens que ganharam o premio nobel\n")

# contar documetos pela bron country

print(f"{db.laureates.count_documents({'bornCountry': 'Brazil'})} Brasileiro(s) ganhou o premio nobel\n")
print(f"{db.laureates.count_documents({'bornCountry': 'United Kingdom'})} Inlgeses ganharam o premio nobel\n")
print(f"{db.laureates.count_documents({'bornCountry': 'France'})} Franceses ganharam o premio nobel\n")



# contar documentos pela data de nascimento antes de 1950
print(f"Existem {db.laureates.count_documents({'born': {'$lt': '1920-01-01'}})} vencedores do premio nobel que nasceram antes de 1920\n")


filter_doc = {
    'bornCountryCode': 'GB', # United Kingdom
    'gender': 'male',
    'diedCountryCode': 'US'
}


print(f"Existem atualmente {db.laureates.count_documents(filter=filter_doc)} ganhadores do premio nobel que sao homens nasceram nos UK e  morreram nos US\n")


# utilizando operador in
filter_in = db.laureates.count_documents(
    {
        'bornCountryCode':{ # coloquei diedcountryCODE, para facilitar a vida so 
            '$in':['GB', 'US', 'JP', 'ZA']
            
        }
    }
)

print(f"atualmente existem {filter_in} vencedores do premio nobel, que nasceram no UK, USA, JP ou STA\n")

# filtrando por pais, porem com esse operador, $in, consigo filtrar por mais de um pais, como nesse exemplo, reino unido, estados unidos, japao, e africa do sul


# filtrando usando o operador ne  NotEqual
filter_en = db.laureates.count_documents({
        'bornCountryCode':{
            '$ne':'US'
    }
})
print(f"Existem {filter_en} vencedores do premio nobel, que nao nasceram nos Estados Unidos\n")

# esse filtro e o oposto do outro, ele filtra quando o valor e diferente de alguma condicaom que nesse caso foi ter nascido nos United States



# 4- Conta documentos que nao possuem uma informacao
no_country = db.laureates.count_documents(
    {
        'bornCountry': {
            '$exists': False
        }
    }
)
print(f"existem {no_country} vencedores do premio nobel que nao se sabe o pais aonde nasceram\n")


estados_unidos = db.laureates.count_documents({
    'bornCountryCode': 'US'
})

print(f"Existem {estados_unidos} estado unidenses vencedores do premio nobel\n")