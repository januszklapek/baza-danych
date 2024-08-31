import json
from userbase import UserBase
from user import User


class UserManager:
    
    def load_users(self):
        try:
            with open('users.json', 'r') as file:
                return {username: UserBase(**data) for username, data in json.load(file).items()}
        except Exception as e:
            print(f"Wystąpił błąd podczas wczytywania danych: {e}")
            return {}

    def save_users(self, users):
        try:
            with open('users.json', 'w') as file:
                json.dump({username: user.to_dict() for username, user in users.items()}, file, indent=4)
        except Exception as e:
            print(f"Wystąpił błąd podczas zapisywania danych: {e}")

    def view_all_users(self):
        users = self.load_users()
        if not users:
            print("Nie udało się wczytać użytkowników.")
            return

        print("\nLista wszystkich użytkowników:")
        for username, details in users.items():
            print(f"Użytkownik: {username}, Rola: {details.role}")

    def add_new_user(self):
        users = self.load_users()

        new_username = input("Podaj nazwę nowego użytkownika: ")
        if new_username in users:
            return "Taki użytkownik już istnieje."

        new_password = input("Podaj hasło dla nowego użytkownika: ")
        new_role = input("Podaj rolę dla nowego użytkownika (admin/user): ")

        if new_role == "admin":
            from admin import Admin
            new_user = Admin(new_username, new_password)
        elif new_role == "user":
            new_user = User(new_username, new_password)
        else:
            return "Nieprawidłowa rola. Użytkownik nie został dodany."

        users[new_username] = new_user
        self.save_users(users)
        return f"Użytkownik {new_username} został dodany."

    def update_user_data(self, admin_username, target_username, new_data):
        users = self.load_users()

        if users[admin_username].role != 'admin':
            return "Brak uprawnień do edycji danych użytkowników."

        if target_username in users:
            user_data = users[target_username]

            # Tu się aktulizują dane użytkownika
            new_username = new_data.get('username', target_username)
            if new_username != target_username:
                users[new_username] = users.pop(target_username)
                target_username = new_username

            user_data.username = new_data.get('username', user_data.username)
            user_data.password = new_data.get('password', user_data.password)
            user_data.role = new_data.get('role', user_data.role)

            self.save_users(users)
            return f"Dane użytkownika {target_username} zostały zaktualizowane."
        else:
            return "Użytkownik nie istnieje."
        
    def delete_user(self, admin_username, target_username):
        users = self.load_users()

        if users[admin_username].role != 'admin':
            return "Brak uprawnień do usunięcia użytkownika."

        if target_username in users:
            if target_username == admin_username:
                return "Nie możesz usunąć swojego własnego konta."

            del users[target_username]
            self.save_users(users)
            return f"Użytkownik {target_username} został usunięty."
        else:
            return "Użytkownik nie istnieje."
