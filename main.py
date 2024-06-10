class User():

    def __init__(self, name, id, access_level):
        self.__name = name
        self.__id = id
        self.__access_level = access_level

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def get_access_level(self):
        return self.__access_level

    def set_access_level(self, access_level):
        self.__access_level = access_level

    def display_info(self):
        print(f"Имя пользоавтеля: {self.__name}, имеет id: {self.__id} и уровень доступа: {self.__access_level}.")

class Admin(User):

    def __init__(self, name, id):
        super().__init__(name, id,'admin ')
        self.__users = {} # {username: [id, access_level]} # def get_users(self) = {} def set_users(self, users) = {} def get_access_level() = {}
    def add_user(self, user):
        self.__users[user.get_name()] = user # {username: [id, access_level]}
        print(f"Добавлен новый пользователь: {user.get_name()}, {user.get_id()}, {user.get_access_level()}.")



    def remove_user(self, username):
        if username in self.__users:
            del self.__users[username]
            print(f"Удален пользователь: {username}")
        else:
            print("Пользователь {username} не найден.")


    def show_users(self):
        print("Список пользователей:")
        for username, user in self.__users.items():
            print(f"Имя: {user.get_name()}, ID: {user.get_id()}, Уровень доступа: {user.get_access_level()}")





user1 = User('Валерий', 22222, "финансист")
user2 = User('Мария', 33333, "кадровик")
user3 = User('Ксения', 44444, "расчетчик")


user1.display_info()
user2.display_info()
user3.display_info()

admin = Admin('Александр', 11111)

admin.add_user(user1)
admin.add_user(user2)
admin.add_user(user3)


admin.show_users()

admin.remove_user('Ксения')

admin.show_users()

admin.remove_user('Борис')

admin.show_users()

