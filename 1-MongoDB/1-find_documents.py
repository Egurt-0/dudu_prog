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


# utilizando operador in
filter_in = db.laureates.count_documents(
    {
        'bornCountryCode':{ # coloquei diedcountryCODE, para facilitar a vida so 
            '$in':['GB', 'US', 'JP', 'ZA']
            
        }
    }
)

print(f"atualmente existem {filter_in} vencedores do premio nobel, que nasceram ou no UK, USA, JP, STA")

# filtrando por pais, porem com esse operador, $in, consigo filtrar por mais de um pais, como nesse exemplo, reino unido, estados unidos, japao, e africa do sul


# filtrando usando o operador ne  NotEqual
filter_en = db.laureates.count_documents({
        'bornCountryCode':{
            '$ne':'US'
    }
})
print(f"Existem {filter_en} vencedores do premio nobel, que nao nasceram nem nos Estados Unidos")

# esse filtro e o oposto do outro, ele filtra quando o valor e diferente de alguma condicaom que nesse caso foi ter nascido nos United States
