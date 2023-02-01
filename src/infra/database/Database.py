from mysql.connector import MySQLConnection
from mysql.connector.pooling import PooledMySQLConnection
from src.core.interfaces.Database import Database as DatabaseInterface

class Database(DatabaseInterface):
    def __init__(self, connection: PooledMySQLConnection | MySQLConnection, database_name, table_name) -> None:
        if not isinstance(database_name, str) or database_name == '':
            raise TypeError('Database Name has not provided')
        if not isinstance(table_name, str) or table_name == '':
            raise TypeError('Tablename has not provided')

        self.__cursor = connection.cursor()
        self.create_database_if_not_exists(database_name)
        pass

    # def setup_database(self, database_name, table_name, *columns):
    #     self.create_database_if_not_exists(database_name)
    #     self.__cursor.execute(f'CREATE TABLE IF NOT EXISTS {database_name}.{table_name} (name VARCHAR(100));')

    def create_database_if_not_exists(self, database_name):
        self.__cursor.execute(f'CREATE DATABASE IF NOT EXISTS {database_name}')

    def create_table(self, table_name, *columns):
        columns = [column for column in [*columns]]
        self.__cursor.execute(f'CREATE TABLE {table_name} (id INTEGER auto_increment primary key);')

        for column in columns:
            self.__cursor.execute(f'ALTER TABLE {table_name} ADD {column};')
