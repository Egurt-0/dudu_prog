from conexao import conexao


cursor_obj =  conexao.cursor()

sql = """
    UPDATE games
    SET NAME = %s
    WHERE ID = %s
    """

cursor_obj.execute(sql, ("EA 25", 7))
conexao.commit()
print("atualizado com sucesso")
conexao.close()