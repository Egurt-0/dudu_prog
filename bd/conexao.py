import psycopg

conexao = psycopg.connect(
    dbname='db_games',
    user='postgres',
    password='dudsWP12',
    host='localhost',
    port='5432'
)
