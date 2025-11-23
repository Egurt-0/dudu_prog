import sqlite3

conexao = sqlite3.connect('titulo.db')
cursor = conexao.cursor()

# excluindo dados

id = (59, 666)

cursor.execute(
    """

        DELETE FROM filmes
        WHERE ID in (?, ?)
    """,
    id
)


conexao.commit()

print("dados exlcuidos com sucesso")