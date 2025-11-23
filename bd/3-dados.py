import sqlite3

# conectando ao banco de dados
while True:
    conexao = sqlite3.connect('titulo.db')
    cursor = conexao.cursor()




# inserindo valores para a tabela(filmes) ja criada
# novamnte, comandos do SQL em maiusculo e o resto em minusculo
    cursor.execute(
    """
    
    INSERT INTO filmes(nome, ano, nota)
    VALUES('duduu', 2010, 67.0)
    """    
    )

    conexao.commit()
    conexao.close()
    print("Dados adicionados na tabela") # retorono para saber se tudo deu certo



