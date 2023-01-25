import unittest

class CreateUserUsecase():
    def execute(self, name, email, password):
        if name == '' or email == '' or password == '':
            raise TypeError('Parameters are not provided correctyly! Fix it!')

class TestCreateUserUsecase(unittest.TestCase):
    def test_it_have_raises_an_error_if_parameters_are_not_provided_correctly(self):
            with self.assertRaises(TypeError) as error:
                CreateUserUsecase().execute(name="", email="", password="")

          
            print(error)
            self.assertEqual('Parameters are not provided correctyly! Fix it!', str(error.exception))


if __name__ == '__main__':
    unittest.main()