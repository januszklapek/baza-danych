from userbase import UserBase
class User(UserBase):
    def __init__(self, username, password):
        super().__init__(username, password, 'user')
