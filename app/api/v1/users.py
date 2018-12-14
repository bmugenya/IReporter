from ...db_con import database_setup
from passlib.hash import pbkdf2_sha256 as sha256


class AdminRegistration(object):

    def __init__(self):
        self.database = database_setup()
        self.cursor = self.database.cursor

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

        self.cursor.execute(query, admin)
        self.database.conn.commit()

        return admin


class UserRegistration(object):

    def __init__(self):
        self.database = database_setup()
        self.cursor = self.database.cursor

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

        self.cursor.execute(query, users)
        self.database.conn.commit()

        return users


class AdminLogin(object):

    def __init__(self):
        self.database = database_setup()
        self.cursor = self.database.cursor

    def login(self, email, password):

        #password = sha256.hash(passwrd)

        users = {
            "email": email,
            "password": password
        }
        query = "SELECT * FROM Users WHERE email = '%s' AND password = '%s';" % (email, password)
        self.cursor.execute(query, users)
        user = self.cursor.fetchall()
        return user


class UserLogin(object):

    def __init__(self):
        self.database = database_setup()
        self.cursor = self.database.cursor

    def login(self, email, password):

        #password = sha256.hash(passwrd)

        users = {
            "email": email,
            "password": password
        }

        query = "SELECT * FROM Users WHERE email = '%s' AND password = '%s';" % (email, password)

        self.cursor.execute(query, users)
        user = self.cursor.fetchall()
        return user
