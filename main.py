from utiles.crud import read, create_user, search, remove, update
from models.data import users

if __name__ == '__main__':

    print(f"Witaj {users[0]['name']}!")
    while True:
        print("menu:")
        print("0. Zakończ program: ")
        print("1.Pokaż co u znajomych: ")
        print("2.Dodaj znajomego: ")
        print("3. Wyszukaj znajomego: ")
        print("4. Usuń znajomego: ")
        print("5. Uaktualnij znajomego: ")
        menu_option: str = input("Wybierz dostępną funkcję z menu: ")
        if menu_option == "0":
            break
        if menu_option == "1":
            read(users)
        if menu_option == "2":
            create_user(users)
        if menu_option == "3":
            search(users)
        if menu_option == "4":
            remove(users)
        if menu_option == "5":
            update(users)









