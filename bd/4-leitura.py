import sqlite3

# 1 conectando no DB
conexao = sqlite3.connect('titulo.db')
cursor = conexao.cursor()

# 2 Leitura de Dados
dados = cursor.execute("SELECT * FROM filmes") # nem falar nada, voce ja sabe
print(dados.fetchall()) # nao sei bem o porque, mas precisamos usar esse fetchall() para poder 
# ter o retorno dos dados de forma legivel. sem ele, o retorno é <sqlite3.Cursor object at 0x000001DD52FA2F40>