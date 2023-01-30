import unittest
from .MockDatabase import MockDatabase

class TestMockDatabase(unittest.TestCase):
    sut = MockDatabase()

    def setUp(self):
        self.sut.clear_database()
        

    def test_it_create_a_new_user(self):
        mock_new_user_data = {'any': 'data'}
        
        new_user = self.sut.create(mock_new_user_data)

        self.assertEqual(new_user, mock_new_user_data)
    
    def test_it_read_all_users(self):
        expected = [{'any1': 'data1'}, {"any2": "data2"}]

        self.sut.create({"any1": "data1"})
        self.sut.create({"any2": "data2"})

        self.assertEqual(self.sut.read_all(), expected)

    def test_it_have_a_clear_database_method(self):
        print(self.sut.database)

        self.sut.create({'any': 'data'})

        self.sut.clear_database()

        self.assertEqual(self.sut.database, [])

        

if __name__ == '__main__':
    unittest.main()