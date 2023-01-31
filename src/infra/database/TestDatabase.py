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
        

    def test_if_hass_passed_connection_database_and_name_of_database_to_init_method(self):
        with self.assertRaises(TypeError) as error:
            Database(connection, database_name='')
          
        self.assertEqual('Connection has not provided', str(error.exception))


if __name__ == '__main__':
    unittest.main()