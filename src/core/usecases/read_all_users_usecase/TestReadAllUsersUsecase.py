import unittest
from src.core.interfaces.Database import Database
from src.core.usecases.mock.mock_database.MockDatabase import MockDatabase

class ReadAllUserUsecase():
    def __init__(self, database: Database):
        if database == '' or database == False or database == None:
            raise TypeError('Database Interface Not Provided')
        
        self.database = database
    
    def execute(self):
        return self.database.read_all()

class TestReadAllUsersUsecase(unittest.TestCase):
    sut = ReadAllUserUsecase(MockDatabase())

    def test_it_return_all_users(self):
        mock_database = MockDatabase()

        mock_database.create({"any1": "data1"})
        mock_database.create({"any2": "data2"})
        mock_database.create({"any3": "data3"})

        self.assertEqual(self.sut.execute(), [{"any1": "data1"}, {"any2": "data2"}, {"any3": "data3"}])

    def test_if_database_interface_has_passed_into_init_method(self):
        with self.assertRaises(TypeError) as error:
            ReadAllUserUsecase(database='')
        
        self.assertEqual('Database Interface Not Provided', str(error.exception))


if __name__ == '__main__':
        unittest.main()