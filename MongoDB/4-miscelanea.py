from  pymongo import MongoClient
from pprint import pprint
from bson.regex import Regex
client = MongoClient()


db = client['nobel']

prizes = db['prizes']
laureates = db['laureates']


fisica_compartilhados = db.laureates.count_documents({
    'prizes':{
        '$elemMatch': { # ajuda a combinar elementos, caracteristicas para ajuda na filtragem
            'category': 'physics',
            'share': '1'
        }
    }
})

print(f"exsitem{fisica_compartilhados} premio de fisica que foram compartihados\n")

antes_de_seila = db.laureates.count_documents({
    'prizes':{
        '$elemMatch': { 
            'category': 'physics',
            'share': '1',
            'year': {'$lt': '1945'}
        }
    }
})


print(f"Existem {antes_de_seila} premios nobeis de fisica que foram publicados antes de 1945\n")




# utilizando Regex
regex = db.laureates.distinct(
    'bornCountry',
    {'bornCountry': {'$regex': 'Poland'}}
)
# print(f"cara, seila {regex}\n")

#  case INSENSITIVE - ou seja, desconsidera maiusculos e minusculos
regex_insensitive = db.laureates.distinct(
    'bornCountry',
    {'bornCountry': {'$regex': 'Poland', '$options': "i"}} # para utilizar o operador voce precisa usar o operardo options e depois usar a opcao i
)
print(f"cara, seila {regex}\n")

# Utilizando classse regex
classe_regex = db.laureates.distinct(
    'bornCountry',
    {'bornCountry': Regex('poland', 'i')}
)
print(f"testando classe regex: {classe_regex}\n")

# starts with
comeca_com = db.laureates.distinct(
    'bornCountry',
    {'bornCountry': Regex('^Poland')} # o ascento do chapeuzinho siginifica comeca com
)

print(f"comeca com Poland {comeca_com}\n")

# Ends with
termina_com = db.laureates.distinct(
    'bornCountry',
    {'bornCountry': Regex('now Poland\)$')} 
)


print(f"termina com now Poland {termina_com}\n")