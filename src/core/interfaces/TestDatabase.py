import unittest
from .Database import Database

class TestDatabaseInterface(unittest.TestCase):
    def test_if_database_interface_have_CRUD_methods(self):
        sut = Database()

        self.assertEqual(sut.create({any: 'data'}), None)
        self.assertEqual(sut.read_all(), None)
        self.assertEqual(sut.update(id=0, data={any: 'data'}), None)
        self.assertEqual(sut.delete(0), None)

if __name__ == '__main__':
    unittest.main()