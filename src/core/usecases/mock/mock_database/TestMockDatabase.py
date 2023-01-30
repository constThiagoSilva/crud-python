import unittest
from .MockDatabase import MockDatabase

class TestMockDatabase(unittest.TestCase):
    def setUp(self):
        self.sut = MockDatabase()

    def test_it_create_a_new_user(self):
        mock_new_user_data = {'any': 'data'}
        
        new_user = self.sut.create(mock_new_user_data)

        self.assertEqual(new_user, mock_new_user_data)

    def test_it_have_a_clear_database_method(self):
        self.sut.create({'any': 'data'})

        self.sut.clear_database()

        self.assertEqual(self.sut.database, [])
        

if __name__ == '__main__':
    unittest.main()