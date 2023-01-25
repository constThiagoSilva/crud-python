import unittest

class Database():
    def create(self):
        pass

class CreateUserUsecase():
    def __init__(self, database):
        if database == '' or database == False:
            raise TypeError('Database not provided! Fix it!')
            
    def execute(self, name, email, password):
        if name == '' or email == '' or password == '':
            raise TypeError('Parameters are not provided correctyly! Fix it!')

class TestCreateUserUsecase(unittest.TestCase):
    def setUp(self):
        self.sut = CreateUserUsecase(Database())

    def test_it_have_an_database_parameter_in_init_def(self):
        with self.assertRaises(TypeError) as error:
            CreateUserUsecase(database='')
          
        self.assertEqual('Database not provided! Fix it!', str(error.exception))
        


    def test_it_have_raises_an_error_if_parameters_are_not_provided_correctly(self):
        with self.assertRaises(TypeError) as error:
            self.sut.execute(name="", email="", password="")
          
        self.assertEqual('Parameters are not provided correctyly! Fix it!', str(error.exception))
    


if __name__ == '__main__':
    unittest.main()