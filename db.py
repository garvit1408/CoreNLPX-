import json


class DataBase:
    def insert(self, name, email, password):
        print(name, email, password)
        with open("users.json", "r") as rf:
            users = json.load(rf)

            if email in users:
                return 0
            else:
                users[email] = [name, password]

        with open("users.json", "w") as wf:
            json.dump(users, wf)
            return 1

    def search(self, email, password):
        with open("users.json", "r") as rf:
            users = json.load(rf)
            if email in users and users[email][1] == password:
                return 1
            else:
                return 0
