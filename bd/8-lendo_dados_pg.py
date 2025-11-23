from conexao import conexao




#  aqui estou apenas
cursor_obj = conexao.cursor()

cursor_obj.execute("SELECT * FROM games")

result = cursor_obj.fetchall()

print(result)