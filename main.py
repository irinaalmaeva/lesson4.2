class User():

    def __init__(self, name, id, access_level):
        self.name = name
        self.id = id
        self.access_level = access_level
        self.users = {}

    def add_user(self, user_name, id, access_level):
        self.users = {user_name: [id, access_level]}
        print(f"Добавлен новый пользователь:{user_name}, {id}, {access_level}.")

    def show_users(self):
        print(self.users)

    def remove_user(self, username):
        if username in self.users:
            del self.users[username]

        print(f"Удален пользователь: {username}")


class Admin(User):
    def __init__(self, name, id, access_level, password):
        super().__init__(name, id, access_level)
        self.password = password



user1 = User('Валерий', 22, 1)
user2 = User('Мария', 33, 2)
user3 = User('Ксения', 44, 1)

user1.add_user('Анна', 55, 2)
user2.add_user('Михаил',66,2)
user3.remove_user('Ксения')