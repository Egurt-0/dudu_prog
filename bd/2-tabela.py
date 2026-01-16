import sqlite3


# nesse caso eu repito essa linha de codigo do arquivo bd.py para conectar essa nova tabela nesse banco de dados. porem
# quando uso esse comando pela primeira vez, ele cria o db, mas na segunda, ja que o db ja existe ele apenas e uma forma de conectar

conexao = sqlite3.connect('titulo.db')


# criando um cursos, que e oque faz nos podermos fazer modificacoes no banco de dados\
cursor = conexao.cursor() # aqui estou apenas criando essa varivavel cursos e definindo ela como o cursos do banco de dados que criamos



# aqui estou criando uma tabela no banco de dados, atraves do cursos.execute
# nessas linhas de codigo a baixo, veremos que todas os comandos do SQL estarao em maiusculo e o que nao for,ou seja, variavei e etc.
# deixaremos em minusculo
cursor.execute(
    """
    CREATE TABLE filmes(
        id INTEGER NOT NULL  PRIMARY KEY AUTOINCREMENT,
        nome TEXTO NOT NULL,
        ano INTERGER NOT NULL,
        nota REAL NOT NULL 
     );




"""    
)

# fechando a conexao
conexao.close()
print("tabela foi criada") # isso serve para vermos se o codigo deu certo, se nao der erro e tudo rodar correto, teremos esse print no final