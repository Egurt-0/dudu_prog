from pymongo import MongoClient



client = MongoClient()
mydb = client.dbposts # criando a connection
mycol = mydb.posts # criando a collection dentro da minhas connection


post1 = {

    "title": "Numpy",
    "categoria": "Matematica com py",
    "level": "intermediario",   
    "autor": {                  # aqui estou criando um dicionario dentro do dicionario, para cara post deve ter o titulo categoria e autor, mas para cada autor deve ter o nome e gmail
        "name": "Einstein",
        "email": "Emcquadrado@gmail.com"
    }

}


result = mycol.insert_one(post1)
print("documento incluido sem problemas")
result
