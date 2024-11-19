from financial_management_system.settings import CONNECTION_MONGODB



class DataBase:
    def __init__(self):
        self.client = CONNECTION_MONGODB
        self.usersdb = self.client["usersdb"]

class UserData(DataBase):
    def __init__(self, username):
        super().__init__()
        self.username = username
    
    def get_data(self):
        userdata = self.usersdb.users.find_one(
            {"_id": self.username}
        )
        return userdata
    
class FinancesData(DataBase):
    def __init__(self, username):
        super().__init__()
        self.username = username
    
    def get_data(self):
        finances_data = self.usersdb.finances.find_one(
            {"_id": self.username}
        )
        
        return finances_data
        
        
# client = MongoClient("localhost", 27017)
# usersdb = client["usersdb"]
# userdata = usersdb.users.find_one({"_id": request.user.username})