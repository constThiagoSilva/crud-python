import unittest

class Database():
    def create(self):
        pass

class CreateUserUsecase():
    def __init__(self, database: Database):
        if database == '' or database == False:
            raise TypeError('Database not provided! Fix it!')

        self.database = database
            
    def execute(self, data: dict):
        if data['name'] == '' or data['email'] == '' or data['password'] == '':
            raise TypeError('Parameters are not provided correctyly! Fix it!')

        return data

class TestCreateUserUsecase(unittest.TestCase):
    def setUp(self):
        self.sut = CreateUserUsecase(Database())


    def test_it_create_a_new_user(self):
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