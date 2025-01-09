import json
import os


class Authentication:
    def __init__(self, user_file="tools/users.json"):
        self.user_file = user_file
        if not os.path.exists(self.user_file):
            with open(self.user_file, "w") as file:
                json.dump({}, file)

    def register_user(self, full_name, username, password):
        with open(self.user_file, "r") as file:
            users = json.load(file)

            if username in users:
                return False

            users[username] = {"full_name": full_name, "password": password}
            with open(self.user_file, "w") as file:
                json.dump(users, file)

            return True

    def authenticate_user(self, username, password):
        with open(self.user_file, "r") as file:
            users = json.load(file)

        if username in users and users[username]["password"] == password:
            return True
        return False
