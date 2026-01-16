from conexao import conexao




#  aqui estou apenas lendo todos os dados do banco de dados, porque nao passei nenhum filtro
cursor_obj = conexao.cursor()

cursor_obj.execute("SELECT * FROM games")

result = cursor_obj.fetchall()

print(result)