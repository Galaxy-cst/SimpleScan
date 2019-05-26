from conf.config import globalConfig, configModifier
import hashlib
import time


class User:
    def __init__(self):
        self.cookie = self.cookie_init()

    def cookie_init(self):
        return hashlib.sha1(str(time.time()).encode('utf-8')).hexdigest()

    def login(self, username, password):
        if username == 'admin' and password == globalConfig['password']:
            return self.cookie
        return False

    def logout(self):
        self.cookie = self.cookie_init()

    def change_password(self, new_password):
        configModifier('password', new_password)
        return True

    def current_user(self, cookie):
        if cookie == self.cookie:
            return 'admin'
        else:
            return False
