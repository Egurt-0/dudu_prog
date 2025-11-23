import sqlite3

# conectar no banco de dados
def conecta_db():
    conexao = sqlite3.connect('titulo.db')
    return conexao

# inserir dados

def insert_data(nome, ano, nota):
    conexao = conecta_db()
    cursor = conexao.cursor()
    cursor.execute(
    """
    
    INSERT INTO filmes(nome, ano, nota)
    VALUES(?, ?, ?)
    """,(nome, ano, nota)    
    )

    conexao.commit()
    conexao.close()


# listagem de dados
def get_data():
    conexao = conecta_db()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM filmes")
    dados = cursor.fetchall()
    cursor.close
    return dados