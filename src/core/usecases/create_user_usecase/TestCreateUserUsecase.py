import unittest
from src.core.usecases.mock.mock_database.MockDatabase import MockDatabase
from src.core.usecases.create_user_usecase.CreateUserUsercase import CreateUserUsecase


class TestCreateUserUsecase(unittest.TestCase):
    def setUp(self):
        self.sut = CreateUserUsecase(MockDatabase())

    @classmethod
    def setUpClass(cls):
        return super().setUpClass()


    def test_it_create_a_new_user_with_same_parameters(self):
        mock_new_user_data = {"name": 'any_name', 'email': 'any_email','password': 'any_password'}
        new_user = self.sut.execute(mock_new_user_data)

        self.assertEqual(new_user, mock_new_user_data)

    def test_it_have_an_database_parameter_in_init_def(self):
        with self.assertRaises(TypeError) as error:
            CreateUserUsecase(database='')
          
        self.assertEqual('Database not provided! Fix it!', str(error.exception))
        


    def test_it_have_raises_an_error_if_parameters_are_not_provided_correctly(self):
        with self.assertRaises(TypeError) as error:
            self.sut.execute({"name": "", "email": "", "password": ""})
          
        self.assertEqual('Parameters are not provided correctyly! Fix it!', str(error.exception))
    


if __name__ == '__main__':
    unittest.main()