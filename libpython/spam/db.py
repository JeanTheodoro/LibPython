from time import sleep


class Session:

    contador = 0
    users = []

    def save(self, user):
        Session.contador += 1
        user.id = Session.contador
        self.users.append(user)

    def list(self):
        print(self.users)
        return self.users

    def rool_back(self):
        self.users.clear()

    def close(self):
        pass


class Conection:

    def __init__(self):
        sleep(2)

    def create_session(self):
        return Session()

    def close(self):
        pass
