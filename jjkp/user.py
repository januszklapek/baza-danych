from userbase import UserBase
class User(UserBase):
    """Klasa użytkownika o standardowej roli."""
    def __init__(self, username, password):
        super().__init__(username, password, 'user')