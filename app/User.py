class User:
    user_id = 0

    def __init__(self, user_id, username, email):
        self.username = username
        self.email = email
        self.user_id = user_id
    
    def getName(self):
        return self.name
    
    def getEmail(self):
        return self.email

    def getUser_id(self):
        return self.user_id
    
    @classmethod
    def getNewUser_id(cls):
        cls.user_id += 1
        return cls.user_id 