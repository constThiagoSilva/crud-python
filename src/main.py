from src.infra.database.connection import connection
from src.infra.database.Database import Database

print("""Olá, esse é seu Gerenciador de Usuários em CMD \n""" + '-' * 60)
database_name = input('Inicie seu banco com um nome: \n')
table_name = input('Agora, insira o nome da tabela: \n')

database = Database(connection, database_name, table_name, 'name VARCHAR(64)', 'email VARCHAR(64)', 'password VARCHAR(64)')

database.drop_database()
database.close_cursor()
