from ...db_con import init_db
from passlib.hash import pbkdf2_sha256 as sha256


class User(object):

    def __init__(self):
        self.user = init_db()

    def save_user(self, firstname, lastname, othernames, email, phoneNumber, username, passwrd):

        password = sha256.hash(passwrd)

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
