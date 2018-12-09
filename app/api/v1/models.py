from ...db_con import init_db


class FlagModel():

    def __init__(self):
        self.db = init_db()

    def save(self, incident, location, comment):
        status = "pending"
        photo = "bribe.jpg"
        video = "bribe.mp4"
        post = {
            "incident": incident,
            "location": location,
            "status": status,
            "photo": photo,
            "video": video,
            "comment": comment
        }

        query = """INSERT INTO Posts  (incident, location,status,photo,video,comments)
                              VALUES(%(incident)s, %(location)s, %(status)s,
                              %(photo)s, %(video)s, %(comment)s)"""
        curr = self.db.cursor()
        curr.execute(query, post)
        self.db.commit()

        return post

    def get(self):
        curr = self.db.cursor()
        curr.execute("SELECT * FROM Posts")
        post = curr.fetchall()
        return post

    def get_flag(self, flag_id):
        curr = self.db.cursor()
        curr.execute("SELECT * FROM Posts WHERE id = (%s);", (flag_id,))

        post = curr.fetchall()
        return post

    def update_flag(self, flag_id, incident, location, comment):
        curr = self.db.cursor()
        post = {
            "incident": incident,
            "location": location,
            "comment": comment

        }
        query = "UPDATE Posts SET incident= '%s',location= '%s', comments='%s' WHERE id = %s;" % (incident, location, comment, flag_id)
        curr.execute(query, post)

        self.db.commit()
        return post

    def save_user(self, firstname, lastname, othernames, email, phoneNumber, username):

        user = {

            "firstname": firstname,
            "lastname": lastname,
            "othernames": othernames,
            "email": email,
            "phoneNumber": phoneNumber,
            "username": username,
            "isAdmin": False,

        }

        query = """INSERT INTO Users  (firstname, lastname,othernames,email,phoneNumber,username,isAdmin)
                              VALUES(%(firstname)s, %(lastname)s, %(othernames)s,
                              %(email)s, %(phoneNumber)s, %(username)s,%(isAdmin)s)"""
        curr = self.db.cursor()
        curr.execute(query, user)
        self.db.commit()

        return user

    def remove_data(self, flag_id):
        curr = self.db.cursor()
        post = curr.execute("DELETE FROM posts WHERE id = (%s);", (flag_id,))
        self.db.commit()

        return post
