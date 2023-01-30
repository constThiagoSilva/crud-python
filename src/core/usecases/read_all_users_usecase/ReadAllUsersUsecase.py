from src.core.interfaces.Database import Database

class ReadAllUserUsecase():
    def __init__(self, database: Database):
        if database == '' or database == False or database == None:
            raise TypeError('Database Interface Not Provided')
        
        self.database = database
    
    def execute(self):
        return self.database.read_all()