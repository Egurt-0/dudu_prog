import sqlite3
import pytest

@pytest.fixture
def db_connection():
    """
    Fixture que configura uma conexao de um banco de dados  SQLITE temporario
    e garante a limpeza dos recursos apos o teste
    """


    conexao = sqlite3.connect(":memory:")# esse :memory: e um comando especial do sqlite para criar um BD na memoria RAM, ou seja temporaria, quando voce desligao pc, tudo some
    cursor = conexao.cursor()

    cursor.execute("""
    CREATE TABLE users(
        id INTEGER PRIMARY KEY,
        name TEXTO NOT NULL,
        email TEXT NOT NULL UNIQUE        
    )
    """
    )
    conexao.commit()
    yield conexao, cursor
    conexao.close()

def test_database_insert(db_connection):
    """
    Testa a insercao de usuarios na tabela users do 
    DB Sqlite    
    """
    conexao, cursor = db_connection
    cursor.execute(
    """
    INSERT INTO users (name, email)
    VALUES (?, ?)
    """,("john Ribeiro", "charliekurk@gmail.com"))
    conexao.commit()

    # verificacao da insercao
    cursor.execute("SELECT * FROM users WHERE email = ?",
                   ("charliekurk@gmail.com", ))
    user = cursor.fetchone()
    assert user is not None
    assert user[1] == "john Ribeiro"
    assert user[2] == "charliekurk@gmail.com"

def test_database_duplicate_emails(db_connection):
    """
    Testa a insercao de usuarios com emails duplicados
    """
    conexao, cursor = db_connection

    cursor.execute(
    """
    INSERT INTO users (name, email)
    VALUES (?, ?)
    """,("Fernando de noronha", "charliekurkgooner@gmail.com"))
    conexao.commit()


    # verificacao de email duplicado
    with pytest.raises(sqlite3.IntegrityError):
        cursor.execute(
        """
        INSERT INTO users (name, email)
        VALUES (?, ?)
        """,("Duplicate users", "charliekurkgooner@gmail.com"))
        conexao.commit()