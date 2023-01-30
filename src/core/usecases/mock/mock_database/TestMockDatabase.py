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

    def test_it_update_an_user(self):
        expected = {"id": 1, "any": "updated_data"}

        self.sut.create({"id": 1, "any": "data"})

        self.assertEqual(self.sut.update(expected["id"], {"any": "updated_data"}), expected)

    def test_it_delete_an_user(self):
        self.sut.create({"id": 1, "any": "data"})
        self.sut.create({"id": 2, "any": "data"})

        self.sut.delete(1)

        self.assertEqual(self.sut.database, [{"id": 2, "any": "data"}])

    def test_it_have_a_clear_database_method(self):
        print(self.sut.database)

        self.sut.create({'any': 'data'})

        self.sut.clear_database()

        self.assertEqual(self.sut.database, [])

        

if __name__ == '__main__':
    unittest.main()