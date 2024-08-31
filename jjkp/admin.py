from userbase import UserBase
from usermanager import UserManager


class Admin(UserBase):
    """Klasa administratora z uprawnieniami do zarządzania użytkownikami."""
    def __init__(self, username, password):
        super().__init__(username, password, 'admin')
        self.user_manager = UserManager()

    def view_all_users(self):
        self.user_manager.view_all_users()

    def add_new_user(self):
        return self.user_manager.add_new_user()

    def update_user_data(self, target_username, new_data):
        return self.user_manager.update_user_data(self.username, target_username, new_data)