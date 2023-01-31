import unittest
from src.infra.database.Database import Database
from src.infra.database.connection import connection

class TestDatabase(unittest.TestCase):
    sut = Database(connection, 'db_users_test')
    

    def test_if_hass_passed_connection_database_and_name_of_database_to_init_method(self):
        with self.assertRaises(TypeError) as error:
            Database(connection, database_name='')
          
        self.assertEqual('Connection has not provided', str(error.exception))


if __name__ == '__main__':
    unittest.main()