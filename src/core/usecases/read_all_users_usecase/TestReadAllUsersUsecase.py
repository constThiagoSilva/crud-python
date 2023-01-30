import unittest
from src.core.interfaces.Database import Database

class ReadAllUserUsecase():
    def __init__(self, database: Database):
        if database == '' or database == False or database == None:
            raise TypeError('Database Interface Not Provided')

class TestReadAllUsersUsecase(unittest.TestCase):
    def test_if_database_interface_has_passed_into_init_method(self):
        with self.assertRaises(TypeError) as error:
            ReadAllUserUsecase(database='')
        
        self.assertEqual('Database Interface Not Provided', str(error.exception))


if __name__ == '__main__':
        unittest.main()