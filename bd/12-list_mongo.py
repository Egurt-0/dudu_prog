from pymongo import MongoClient
from pprint import pprint

client = MongoClient() # se conectando com o mongodb

mydb = client.dbposts # essa connection ja foi criada, ou seja, ele esta apenas se conectando
mycol = mydb.posts # mesma coisa vale para essa collection aqui


#  retornar todos os documentos
retorna_tudo = mycol.find() # isso faz ele retornar todos os documentos
# retorno_primeiro = mycol.find_one() # retorna apenas o primerio

for r in retorna_tudo: # preciso fazer esse loop para poder ler o retorno, caso contrario ele retorna object at 0x0000016B0E6AF770>
    pprint(r) # uso o pprint para deixar melhor para ler, ele e um modulo para a impressao mais bonita dos dados