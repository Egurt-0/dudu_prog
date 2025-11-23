from sqlalchemy import create_engine, Column, Integer, String, Float # lembre-se de sempre ter certeza de que voce imporou a coisa certa, tipo Column != de column, se voce esquecer dessa letra maiscula voce ja esta importando algo totalmente diferente
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine("sqlite:///banco.db", echo=True)
Base = declarative_base()



class Filme(Base):  # criando a tabela com atraves de uma classe, e definindo o tipo de valor de cada variavel
    __tablename__ = "filmes"
    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    ano = Column(Integer, nullable=False)
    nota = Column(Float, nullable=False) # nesse caso, o erro que tinha cometido, foi escrever float e nao Float, so a letra maiuscula faz toda diferenca,esses modulos tem um formato bem especifico que deve ser seguido a risca


Base.metadata.create_all(engine) 


# inserindo filmes
def add_films(nome, ano, nota): # funcao para adicionar um filme
    Session = sessionmaker(bind=engine)
    session = Session()
    filme = Filme(nome=nome, ano=ano, nota=nota)
    session.add(filme)
    session.commit()
    session.close()


add_films("Dudu, principe do python", 2010, 10.5) # adicionando um exemplo de filme. voce passa add_films("nome"(str), ano(int), nota(float))


# funcao para atualizacao de um filme
def update_data(id, nome=None, ano=None, nota=None):
    Session = sessionmaker(bind=engine)
    session = Session()
    filme = session.query(Filme).filter_by(id=id).first()
    if filme:
        if nome is not None:
            filme.nome = nome
        if ano is not None:
            filme.ano = ano
        if nota is not None:
            filme.nota = nota   
        session.commit()
        session.close()




update_data(1, "Homem aranha", 2001, 7.8) # nsse caso, como e um update, estou substituindo valores de uma coluna, entao preciso identificar qual coluna, para isso uso o id, que sao como o index de cada coluna
# entao:  update_data(id(index), "novo_nome"(str), novo_ano(int), nova_nota(float))



def delete_film(id):
    Session = sessionmaker(bind=engine)
    session = Session()
    filme = session.query(Filme).filter_by(id=id).first()
    if filme:
        session.delete(filme) # esse e o mais simples de todos, apenas reutilizei esse filtro por id(index) e se o filme com esse id existir(if filme:) ele deleta o filme
    
    session.commit()
    session.close()

delete_film(67)
# para executar, apenas uso delete_film(id do filme)
# ex delete_film(6327), se eu executar, ele exclui a coluna com id 6327