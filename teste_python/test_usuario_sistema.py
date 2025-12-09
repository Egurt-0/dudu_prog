import pytest
import sqlite3
import usuario_sistema

                         
@pytest.fixture
def db_connection():
    """
    Fixture que configura uma conexao de um banco de dados  SQLITE temporario
    e garante a limpeza dos recursos apos o teste
    
    """

    conexao = sqlite3.connect(":memory:")# esse :memory: e um comando especial do sqlite para criar um BD na memoria RAM, ou seja temporaria, quando voce desligao pc, tudo some
    cursor = conexao.cursor()

    cursor.execute("""
    CREATE TABLE usuarios(
        id INTEGER PRIMARY KEY,
        name TEXTO NOT NULL,
        email TEXT NOT NULL UNIQUE        
    )
    """
    )
    conexao.commit()
    yield conexao, cursor
    conexao.close()

@pytest.mark.parametrize(
    "id, name, email, name_esperado",
    [
            (1, "Nome", "nome@email.com", "Nome"),
            (2, "Aurelio", "aureliofagundes@email.com", "Aurelio"),
            (3, "Socrates", "soc@platao.com", "Socrates")
    ]
)

@pytest.mark.unit
def test_adicionar_usuario(db_connection, id, name, email, name_esperado):
    conn, cursor = db_connection
    usuario_sistema.adicionar_usuario(cursor, id, name, email)
    resultado = usuario_sistema.buscar_usuario(cursor, email)
    assert resultado is not None
    assert resultado[1] == name_esperado
    assert resultado[2] == email

@pytest.mark.integration
def test_buscar_usuario_com_email_inexistente(db_connection):
    conn, cursor= db_connection
    resultado = usuario_sistema.buscar_usuario(cursor, "naoexistente@email.com")
    assert resultado is None
    
@pytest.mark.slow
@pytest.mark.integration
def adiocionar_buscar_muitos_usuarios(db_connection):
    import time
    conn, cursor = db_connection
    for i in range(100):
        usuario_sistema.adicionar_usuario(cursor, i, f"User{i}", f"User{i}@gmail.com")
    cursor.commit()

    time.sleep(2)

    for i in range(100):
        resultado = usuario_sistema.buscar_usuario(cursor,  f"User{i}@gmail.com")

        assert resultado is not None
        assert resultado[2] == f"User{i}"
        assert resultado[4] == f"User{i}@gmail.com"
    cursor.close()