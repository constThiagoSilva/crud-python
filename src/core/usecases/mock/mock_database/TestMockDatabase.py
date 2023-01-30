import unittest
from .MockDatabase import MockDatabase

class TestMockDatabase(unittest.TestCase):
    def setUp(self):
        self.sut = MockDatabase()

    def test_it_create_a_new_user(self):
        mock_new_user_data = {'any': 'data'}

        new_user = self.sut.create(mock_new_user_data)

        self.assertEqual(new_user, mock_new_user_data)
        

if __name__ == '__main__':
    unittest.main()