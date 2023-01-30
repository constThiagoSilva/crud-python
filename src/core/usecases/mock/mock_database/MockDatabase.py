from src.core.interfaces.Database import Database

class MockDatabase(Database):
    __database = []

    def create(self, data: dict):
        self.database.append(data)

        return data  

    def read_all(self):
        return self.database

    def update(self, id: int, data: dict):
        for user in self.database:
            if user['id'] == id:
                user = {"id": user["id"], **data} 
                return user
    def delete(self, id):
        for index, user in enumerate(self.database):
            if user['id'] == id:
                del self.database[index]
                

    def clear_database(self):
        self.database = []

    @property
    def database(self):
        return self.__database

    @database.setter
    def database(self, value):
        self.__database = value