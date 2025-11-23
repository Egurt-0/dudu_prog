import sqlite3

# conectando banco de dados ---- todas vez que voce quer fazer uma acao se conectando com um banco de dados
# especifico, voce precisa fazer essas duas linhas de codigo, simples porem fundamentais
conexao = sqlite3.connect('titulo.db')
cursor = conexao.cursor()


# atualizando os dados

id = 67 # definindo o id do item que quero atualizar
cursor.execute( # comandos do SQL em maiusculo e variaveis em minusculo
    """

    UPDATE filmes SET nome = ?
    WHERE id = ?
    """,
# aqui |  nessa virgula, acabei o codigo SQL e agora estou definindo os novos valores para serem atualizados
    ("DEDE o palmerence mais coxa do mundo", id) # aqui estou passando os 2 parametros que ele precisa
    # antes estavam como ? agora nesse parenteses eu os defino, nao coloco id como um numero, pois ja defini a variavel como um numero
)

conexao.commit()

print("Dados atualizados")



# escrevendo sobre a linha 15, na linha 15 eu poderia escrever qualquer valor da lista que queria atualizar como -> valor = ?
# nesse caso, queria atualizar o nome, entao coloquei nome = ? e depois nos parenteses embaixo coloquei o novo valor, para sobrepor o antigo
# mas eu posso fazer isso como qualquer valor da lista,por exemplo: nota = ? e nos parenteses coloco a nota que quero sobrepor a antiga

# linha 16 , eu apenas digo que ele so vai aplicar essas alteracoes, fazer esse update, aonde o id for igual a ?
# nesse caso o id que escolhi foi 67
# ou seja, ele so vai alterar o nome da lista que tem o id 67, mas nenhuma