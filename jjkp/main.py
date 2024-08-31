import time

from user import User
from admin import Admin


def login(username, password):
    from usermanager import UserManager
    """Logowanie użytkownika i zwrócenie jego obiektu."""
    user_manager = UserManager()
    users = user_manager.load_users()
    if username in users and users[username].password == password:
        user = users[username]
        if user.role == 'admin':
            return f"Zalogowano jako administrator: {username}", Admin(user.username, user.password)
        elif user.role == 'user':
            return f"Zalogowano jako użytkownik: {username}", User(user.username, user.password)
    return "Nieprawidłowa nazwa użytkownika lub hasło.", None

def admin_menu(admin):
    """Menu dla administratora pozwalające na zarządzanie użytkownikami."""
    from usermanager import UserManager

    user_manager = UserManager()
    
    while True:
        print("\n--- MENU ADMINISTRATORA ---")
        print("1. Zobacz wszystkich użytkowników")
        print("2. Dodaj nowego użytkownika")
        print("3. Usuń użytkownika")
        print("4. Zmień nazwę użytkownika")
        print("5. Zmień hasło użytkownika")
        print("6. Zmień rolę użytkownika")
        print("7. Wyjdź")
        choice = input("Wybierz opcję: ")

        if choice == '7':
            print("Wylogowano.")
            break

        if choice == '1':
            time.sleep(0.75)
            admin.view_all_users()
        elif choice == '2':
            time.sleep(0.75)
            add_message = admin.add_new_user()
            print(add_message)
        elif choice == '3':
            time.sleep(0.75)
            target_username = input("Podaj nazwę użytkownika, którego chcesz usunąć: ")
            delete_message = user_manager.delete_user(admin.username, target_username)
            time.sleep(0.45)
            print(delete_message)
        elif choice in ['4', '5', '6']:
            target_username = input("Podaj nazwę użytkownika, którego dane chcesz zmienić: ")
            new_data = {}

            if choice == '4':
                time.sleep(0.75)
                new_username = input("Podaj nową nazwę użytkownika: ")
                new_data['username'] = new_username
            elif choice == '5':
                time.sleep(0.75)
                new_password = input("Podaj nowe hasło: ")
                new_data['password'] = new_password
            elif choice == '6':
                time.sleep(0.75)
                new_role = input("Podaj nową rolę (admin/user): ")
                new_data['role'] = new_role

            update_message = admin.update_user_data(target_username, new_data)
            print(update_message)
        else:
            print("Nieprawidłowy wybór, spróbuj ponownie.")

username_input = input("Podaj nazwę użytkownika: ")
password_input = input("Podaj hasło: ")

login_message, logged_in_user = login(username_input, password_input)
print(login_message)

if isinstance(logged_in_user, Admin):
    admin_menu(logged_in_user)
