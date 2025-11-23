from conexao import conexao

cursor_opj = conexao.cursor()

games = [ 
    ('Jedi Fallen order', 2023, 8.0),
    ('dario games, 2025', 2020, 9.7)

]



for game in games:
    cursor_opj.execute(
        """
       
        INSERT INTO games(name, year, score)
        VALUES (%s, %s, %s)
        """, game
    )

    
conexao.commit()
print("dados inseridos meu lindao")
conexao.close()