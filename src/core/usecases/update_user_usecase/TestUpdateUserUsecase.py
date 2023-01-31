import unittest
from src.core.interfaces.Database import Database

class UpdateUserUsecase:
    def __init__(self, database: Database) -> None:
        if database == '' or database == False or database == None:
            raise ValueError('Database Interface Not Provided')

class TestUpdateUserUsecase(unittest.TestCase):
    def test_if_database_interface_has_passed_into_init_method(self):
        with self.assertRaises(ValueError) as error:
            UpdateUserUsecase(database='')
            
        self.assertEqual('Database Interface Not Provided', str(error.exception))

if __name__ == '__main__':
    unittest.main()