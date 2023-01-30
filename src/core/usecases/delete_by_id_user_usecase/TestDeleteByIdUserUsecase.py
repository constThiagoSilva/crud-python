import unittest
from src.core.interfaces.Database import Database

class DeleteByIdUserUsecase:
    def __init__(self, database: Database):
        if database == '' or database == False or database == None:
            raise ValueError('Database Interface Not Provided')
        
        self.database = database

class TestDeleteByIdUserUsecase(unittest.TestCase):
    def test_if_database_interface_has_passed_into_init_method(self):
        with self.assertRaises(ValueError) as error:
            DeleteByIdUserUsecase(database='')
            
        self.assertEqual('Database Interface Not Provided', str(error.exception))

if __name__ == '__main__':
    unittest.main()