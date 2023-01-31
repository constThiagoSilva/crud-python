import unittest
from src.infra.database.Database import Database
from src.infra.database.connection import connection

class TestDatabase(unittest.TestCase):
    sut = Database(connection, 'db_users_test')
    cursor = connection.cursor()

    def test_it_create_a_database_if_not_exists(self):
        databases_list = []

        self.sut.create_database_if_not_exists('new_test_db')
        self.cursor.execute('SHOW DATABASES')

        for db in self.cursor:
            for tuple in db:
                databases_list.append(tuple)

        self.assertIn('new_test_db', databases_list)

        self.cursor.execute('DROP DATABASE new_test_db')
        self.cursor.close()
        

    def test_if_has_passed_name_of_database_to_created_and_table_name_to_init_method(self):
        with self.assertRaises(TypeError) as error:
            Database(connection, database_name='', table_name='any')
          
        self.assertEqual('Database Name has not provided', str(error.exception))

        with self.assertRaises(TypeError) as error:
            Database(connection, database_name='any', table_name='')
          
        self.assertEqual('Tablename has not provided', str(error.exception))


if __name__ == '__main__':
    unittest.main()