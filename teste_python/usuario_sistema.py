def adicionar_usuario(cursor, id , name, email):
    """Adiciona um usuario ao banco de dados"""
    cursor.execute('''
            INSERT INTO usuarios(id, name, email) VALUES (?, ?, ?)
    ''', (id, name, email))




def buscar_usuario(cursor, email):
    """Busca um usuario pelo email"""
    cursor.execute("SELECT * FROM usuarios WHERE email = ? ", (email, ))

    return cursor.fetchone()