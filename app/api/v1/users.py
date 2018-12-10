from ...db_con import init_db
from passlib.hash import pbkdf2_sha256 as sha256


class AdminRegistration(object):

    def __init__(self):
        self.user = init_db()

    def save_admin(self, firstname, lastname, othernames, email, phoneNumber, username, password):

       # password = sha256.hash(passwrd)

        admin = {

            "firstname": firstname,
            "lastname": lastname,
            "othernames": othernames,
            "email": email,
            "phoneNumber": phoneNumber,
            "username": username,
            "isAdmin": True,
            "password": password

        }

        query = """INSERT INTO Users  (firstname, lastname,othernames,email,phoneNumber,username,isAdmin,password)
                              VALUES(%(firstname)s, %(lastname)s, %(othernames)s,
                              %(email)s, %(phoneNumber)s, %(username)s,%(isAdmin)s,%(password)s)"""
        curr = self.user.cursor()
        curr.execute(query, admin)
        self.user.commit()

        return admin


class UserRegistration(object):

    def __init__(self):
        self.user = init_db()

    def save_user(self, firstname, lastname, othernames, email, phoneNumber, username, password):

        #password = sha256.hash(passwrd)

        users = {

            "firstname": firstname,
            "lastname": lastname,
            "othernames": othernames,
            "email": email,
            "phoneNumber": phoneNumber,
            "username": username,
            "isAdmin": False,
            "password": password

        }

        query = """INSERT INTO Users  (firstname, lastname,othernames,email,phoneNumber,username,isAdmin,password)
                              VALUES(%(firstname)s, %(lastname)s, %(othernames)s,
                              %(email)s, %(phoneNumber)s, %(username)s,%(isAdmin)s,%(password)s)"""
        curr = self.user.cursor()
        curr.execute(query, users)
        self.user.commit()

        return users


class AdminLogin(object):

    def __init__(self):
        self.user = init_db()

    def login(self, email, password):

        #password = sha256.hash(passwrd)

        users = {
            "email": email,
            "password": password
        }
        query = "SELECT * FROM Users WHERE email = '%s' AND password = '%s';" % (email, password)
        curr = self.user.cursor()
        curr.execute(query, users)
        user = curr.fetchall()
        return user


class UserLogin(object):

    def __init__(self):
        self.user = init_db()

    def login(self, email, password):

        #password = sha256.hash(passwrd)

        users = {
            "email": email,
            "password": password
        }

        curr = self.user.cursor()
        query = "SELECT * FROM Users WHERE email = '%s' AND password = '%s';" % (email, password)

        curr = self.user.cursor()
        curr.execute(query, users)
        user = curr.fetchall()
        return user
