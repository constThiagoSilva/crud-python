import unittest
from src.infra.database.Database import Database
from src.infra.database.connection import connection

class TestDatabase(unittest.TestCase):
    sut = Database(connection, 'db_users_test', 'tb_users_test', 'name VARCHAR(64)', 'email VARCHAR(64)', 'password VARCHAR(64)')
    cursor = connection.cursor()

    def tearDown(self) -> None:
        self.cursor.execute('DELETE FROM db_users_test.tb_users_test')

    @classmethod
    def tearDownClass(cls) -> None:
        cls.cursor.execute('DROP DATABASE db_users_test')
        cls.cursor.close()
        cls.sut.close_cursor()

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


    def test_it_read_all_users(self):
        users_in_sql_list = []

        self.sut.create(("any_name1", "any1@gmail.com", 'any_password1'))
        self.sut.create(("any_name2", "any2@gmail.com", 'any_password2'))
        self.sut.create(("any_name3", "any3@gmail.com", 'any_password3'))

        users = self.sut.read_all()
        self.cursor.execute('SELECT * FROM db_users_test.tb_users_test')

        for users_in_sql in self.cursor:
            users_in_sql_list.append(users_in_sql)

        self.assertEqual(users, users_in_sql_list)


    def test_it_update_an_user(self):
        user_update_data = ('other_name', 'other@gmail.com', 'any_password')
        user_updated = ()
        self.sut.create(("any_name", "any@gmail.com", 'any_password'))
        self.cursor.execute("SELECT id FROM db_users_test.tb_users_test where name = 'any_name'")

        for user_id_to_be_updated in self.cursor:
            user_updated = self.sut.update(user_id_to_be_updated[0], user_update_data)

        self.cursor.execute("SELECT * FROM db_users_test.tb_users_test")
        for possibility_user_updated in self.cursor:
            self.assertEqual(user_updated, possibility_user_updated)
        
    
    def test_it_delete_an_user_by_id(self):
        self.sut.create(("any_name", "any@gmail.com", 'any_password'))
        self.cursor.execute("SELECT id FROM db_users_test.tb_users_test where name = 'any_name'")

        for user_id_to_be_deleted in self.cursor:
            self.sut.delete(user_id_to_be_deleted[0])

        user_deleted = None
        self.cursor.execute("SELECT * FROM db_users_test.tb_users_test")
        for possibily_user_deleted in self.cursor:
            user_deleted = possibily_user_deleted
            
        self.assertIsNone(user_deleted)



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