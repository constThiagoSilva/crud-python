import unittest
from src.infra.database.Database import Database
from src.infra.database.connection import connection

class TestDatabase(unittest.TestCase):
    sut = Database(connection, 'db_users_test', 'tb_users_test', 'name VARCHAR(64)', 'email VARCHAR(64)', 'password VARCHAR(64)')
    cursor = connection.cursor()

    def setUp(self):
        self.cursor = connection.cursor()

    def test_it_create_a_database_if_not_exists(self):
        databases_list = []

        self.sut.create_database_if_not_exists('any_db')
        self.cursor.execute('SHOW DATABASES')

        for db in self.cursor:
            for tuple in db:
                databases_list.append(tuple)

        self.assertIn('any_db', databases_list)

        self.cursor.execute('DROP DATABASE any_db')


    def test_it_create_a_table_with_columns_passed_by_arguments(self):
        tables_list = []

        self.sut.create_database_if_not_exists('any_db')
        self.cursor.execute('USE any_db')
        self.sut.create_table('any_tb', 'name VARCHAR(20) not null', 'age INTEGER')
        self.cursor.execute('SHOW TABLES')

        for tables_in_any_db in self.cursor:
            for tuple in tables_in_any_db:
                tables_list.append(tuple)

        self.assertIn('any_tb', tables_list)

        self.cursor.execute('DROP DATABASE any_db')

    def test_it_create_an_user(self):
        user_to_be_created = ("any_name", "any@gmail.com", "any_pass")

        user = self.sut.create(user_to_be_created)
        self.cursor.execute('SELECT * FROM db_users_test.tb_users_test')

        for user_in_sql in self.cursor:
            self.assertEqual(user, user_in_sql)

        self.cursor.execute('DROP DATABASE db_users_test')
        


class TestDatabaseConstructor(unittest.TestCase):
    def test_if_has_passed_name_of_database_to_created_and_table_name_to_init_method(self):
        with self.assertRaises(TypeError) as error:
            Database(connection, database_name='', table_name='any')
          
        self.assertEqual('Database Name has not provided', str(error.exception))

        with self.assertRaises(TypeError) as error:
            Database(connection, database_name='any', table_name='')
          
        self.assertEqual('Tablename has not provided', str(error.exception))

if __name__ == '__main__':
    unittest.main()