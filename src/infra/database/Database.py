from mysql.connector import MySQLConnection
from mysql.connector.pooling import PooledMySQLConnection
import uuid
from src.core.interfaces.Database import Database as DatabaseInterface

class Database(DatabaseInterface):
    def __init__(self, connection: PooledMySQLConnection | MySQLConnection, database_name, table_name, *columns) -> None:
        if not isinstance(database_name, str) or database_name == '':
            raise TypeError('Database Name has not provided')
        if not isinstance(table_name, str) or table_name == '':
            raise TypeError('Tablename has not provided')

        self.connection = connection
        self.__cursor = connection.cursor()
        self.database_name = database_name
        self.table_name = table_name

        self.setup_database(database_name, table_name, *columns)


    def setup_database(self, database_name, table_name, *columns):
        self.create_database_if_not_exists(database_name)
        self.__cursor.execute(f'USE {database_name}')
        self.create_table(table_name, *columns)

    def create(self, data: tuple):
        id = uuid.uuid4()
        self.__cursor.execute(f"INSERT INTO {self.database_name}.{self.table_name} (id, name, email, password) VALUES ('{id}', '{data[0]}', '{data[1]}', '{data[2]}');")
        self.connection.commit()

        self.__cursor.execute(f"SELECT * FROM db_users_test.tb_users_test WHERE id = '{id}'")

        for user in self.__cursor:
            return user

    def read_all(self):
        self.__cursor.execute(f'SELECT * FROM {self.database_name}.{self.table_name}')

        return [users for users in self.__cursor]

    def delete(self, id):
        self.__cursor.execute(f"DELETE FROM {self.database_name}.{self.table_name} where id = '{id}'")

    def create_database_if_not_exists(self, database_name):
        self.__cursor.execute(f'CREATE DATABASE IF NOT EXISTS {database_name}')

    def create_table(self, table_name, *columns):
        columns = [column for column in [*columns]]
        self.__cursor.execute(f'CREATE TABLE IF NOT EXISTS {table_name} (id VARCHAR(40) primary key);')

        for column in columns:
            self.__cursor.execute(f'ALTER TABLE {table_name} ADD {column};')
