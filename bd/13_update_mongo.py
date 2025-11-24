from pymongo import MongoClient

client = MongoClient()

mydb = client.dbposts # faco isso sempre, para definir aonde vao ocorrer as alteracoes, nesse caso, na connection dbposts e na collection posts
mycol = mydb.posts # definindo qual collection vou fazer as alteraceos


old_level = {   "level": "intermediario"}
new_level = { "$set": {"level": "iniciante"}}


mycol.update_one(old_level, new_level)
for x in mycol.find():
    print(x)