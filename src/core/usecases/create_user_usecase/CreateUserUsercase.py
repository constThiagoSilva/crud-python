from src.core.interfaces.Database import Database

class CreateUserUsecase():
    def __init__(self, database: Database):
        if database == '' or database == False:
            raise TypeError('Database not provided! Fix it!')

        self.database = database
            
    def execute(self, data: dict):
        if data['name'] == '' or data['email'] == '' or data['password'] == '':
            raise TypeError('Parameters are not provided correctyly! Fix it!')

        return self.database.create(data)