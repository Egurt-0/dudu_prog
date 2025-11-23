from conexao import conexao

cursor_obj = conexao.cursor()


sql = """

    DELETE FROM games
    WHERE ID = %s
    """


cursor_obj.execute(sql, (2, )) # precisa colocar a virugla e o espaco, para que ele reconheca como uma tupla, se deixar so o numero sozinho, ele da erro
conexao.commit()
print("deu tudo certo, coluna excluida com sucesso")
conexao.close()