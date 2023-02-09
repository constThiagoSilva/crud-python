from src.infra.database.connection import connection
from src.infra.database.Database import Database
from src.core.usecases.read_all_users_usecase.ReadAllUsersUsecase import ReadAllUserUsecase

print("""Olá, esse é seu Gerenciador de Usuários em CMD \n""" + '-' * 60)
database_name = input('Inicie seu banco com um nome: \n')
table_name = input('Agora, insira o nome da tabela: \n')

database = Database(connection, database_name, table_name, 'name VARCHAR(64)', 'email VARCHAR(64)', 'password VARCHAR(64)')

database.create(('Thiago', 'thi@gmail.com', '123'))
database.create(('Jorge', 'jor@gmail.com', '123'))

while True:
    print("""\nEscolha uma opção \n
[1] - Adicionar um usuário      [3] - Ler usuários
[2] - Atualizar um usuário      [4] - Deletar um usuário""")

    users_choice = int(input())

    match users_choice:
        case 1:
            print('Add')
        case 2:
            print('Up')
        case 3:
            users = ReadAllUserUsecase(database).execute()
            print(users)
            
        case 4:
            print('Del')
        case _:
            print('INisra um dos numeros')

    break

database.drop_database()
database.close_cursor()
