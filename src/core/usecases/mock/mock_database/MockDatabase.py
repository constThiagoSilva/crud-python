from src.core.interfaces.Database import Database

class MockDatabase(Database):
    __database = []

    def create(self, data: dict):
        self.database.append(data)

        return data        

    @property
    def database(self):
        return self.__database

    @database.setter
    def database(self, value):
        self.__database = value