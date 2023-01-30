import unittest
from src.core.usecases.mock.mock_database.MockDatabase import MockDatabase
from src.core.interfaces.Database import Database

class DeleteByIdUserUsecase:
    def __init__(self, database: Database):
        if database == '' or database == False or database == None:
            raise ValueError('Database Interface Not Provided')
        
        self.database = database
    
    def execute(self, id: int):
        if not isinstance(id, int) or id <= 0:
            raise ValueError('Parameter Id not Provided Correctly')

class TestDeleteByIdUserUsecase(unittest.TestCase):
    def test_if_parameter_id_has_provided_correctly_to_execute_method(self):
        with self.assertRaises(ValueError) as error:
            sut = DeleteByIdUserUsecase(MockDatabase)
            sut.execute(id=0)
        
        self.assertEqual('Parameter Id not Provided Correctly', str(error.exception))

    def test_if_database_interface_has_passed_into_init_method(self):
        with self.assertRaises(ValueError) as error:
            DeleteByIdUserUsecase(database='')
            
        self.assertEqual('Database Interface Not Provided', str(error.exception))

if __name__ == '__main__':
    unittest.main()