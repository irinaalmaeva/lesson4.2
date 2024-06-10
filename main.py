class User():

    def __init__(self, name, id, access_level):
        self.name = name
        self.id = id
        self.access_level = access_level
        self.users = {}

    def add_user(self, username, id, access_level):
        self.users = {username: [id, access_level]}
        print(f"Добавлен новый пользователь:{username}, {id}, {access_level}.")

    def show_users(self , self_users = None):
        print(f"Добавлен пользователь: {self.users}")

    def remove_user(self, username):
        if username in self.users:
            del self.users[username]

        print(f"Удален пользователь: {username}")





user1 = User('Валерий', 22222, "финансист")
user2 = User('Мария', 33333, "кадровик")
user3 = User('Ксения', 44444, "расчетчик")

print(f"Имя пользоавтеля: {user1.name}, имеет id: {user1.id} и уровень доступа: {user1.access_level}.")
print(f"Имя пользоавтеля: {user2.name}, имеет id: {user2.id} и уровень доступа: {user2.access_level}.")
print(f"Имя пользоавтеля: {user3.name}, имеет id: {user2.id} и уровень доступа: {user2.access_level}.")


user1.add_user('Борис',66666,"финансист")
user2.add_user('Анна', 55555, "кадровик")
user3.add_user('Михаил',77777,"расчетчик")


user1.show_users()
user2.show_users()
user3.show_users()

user1.remove_user('Борис')

