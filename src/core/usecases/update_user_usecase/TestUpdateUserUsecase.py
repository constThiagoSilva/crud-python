import unittest
from src.core.interfaces.Database import Database
from src.core.usecases.mock.mock_database.MockDatabase import MockDatabase

class UpdateUserUsecase:
    def __init__(self, database: Database) -> None:
        if database == '' or database == False or database == None:
            raise ValueError('Database Interface Not Provided')

        self.database = database

    def execute(self, id: int, data: dict):
        if not isinstance(id, int) or id <= 0:
            raise ValueError('Parameter Id not Provided Correctly')
        if not isinstance(data, dict) or data == {}:
            raise ValueError('Parameter Data not Provided Correctly')

        return self.database.update(id, data)

class TestUpdateUserUsecase(unittest.TestCase):
    sut = UpdateUserUsecase(MockDatabase())

    def test_it_update_an_user(self):
        expected = {"id": 1, "any": "data_updated"}
        mock_database = MockDatabase()

        mock_database.create({"id": 1, "any1": "data"})

        updated_user = self.sut.execute(1, {"any": "data_updated"})

        self.assertEqual(updated_user, expected)

    def test_if_parameter_id_and_data_has_provided_correctly_to_execute_method(self):
        with self.assertRaises(ValueError) as error:
            self.sut.execute(id=0, data={"any": "data"})
        
        self.assertEqual('Parameter Id not Provided Correctly', str(error.exception))

        with self.assertRaises(ValueError) as error:
            self.sut.execute(id=1, data={})
        
        self.assertEqual('Parameter Data not Provided Correctly', str(error.exception))

    def test_if_database_interface_has_passed_into_init_method(self):
        with self.assertRaises(ValueError) as error:
            UpdateUserUsecase(database='')
            
        self.assertEqual('Database Interface Not Provided', str(error.exception))

if __name__ == '__main__':
    unittest.main()