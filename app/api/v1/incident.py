from ...db_con import database_setup


class PostIncidents():

    def __init__(self):
        self.database = database_setup()
        self.cursor = self.database.cursor

    def save(self, post_type, location, comment):
        status = "pending"
        photo = "bribe.jpg"
        video = "bribe.mp4"
        post = {
            "post_type": post_type,
            "location": location,
            "status": status,
            "photo": photo,
            "video": video,
            "comment": comment
        }

        query = """INSERT INTO Posts  (post_type, location,status,photo,video,comments)
                              VALUES(%(post_type)s, %(location)s, %(status)s,
                              %(photo)s, %(video)s, %(comment)s)"""

        self.cursor.execute(query, post)
        self.database.conn.commit()

        return post


class ViewIncidents():
    def __init__(self):
        self.database = database_setup()
        self.cursor = self.database.cursor

    def get(self):

        self.cursor.execute("SELECT * FROM Posts")
        post = self.cursor.fetchall()
        return post


class ViewIncident():

    def __init__(self):
        self.database = database_setup()
        self.cursor = self.database.cursor

    def get_flag(self, flag_id):

        self.cursor.execute("SELECT * FROM Posts WHERE id = (%s);" % (flag_id,))

        post = self.cursor.fetchall()
        return post


class UpdateIncident():

    def __init__(self):
        self.database = database_setup()
        self.cursor = self.database.cursor

    def update_map(self, flag_id, location):

        post = {
            "location": location,
        }
        query = "UPDATE Posts SET location= '%s' WHERE id = %s;" % (location, flag_id)
        self.cursor.execute(query, post)

        self.database.conn.commit()
        return post

    def update_post(self, flag_id, comment):
        post = {
            "comment": comment,
        }
        query = "UPDATE Posts SET comments= '%s' WHERE id = %s;" % (comment, flag_id)
        self.cursor.execute(query, post)

        self.database.conn.commit()
        return post

    def update_status(self, flag_id, status):
        post = {
            "status": status,
        }
        query = "UPDATE Posts SET status= '%s' WHERE id = %s;" % (status, flag_id)
        self.cursor.execute(query, post)

        self.database.conn.commit()
        return post


class RemoveIncident():

    def __init__(self):
        self.database = database_setup()
        self.cursor = self.database.cursor

    def remove_data(self, flag_id):
        post = self.cursor.execute("DELETE FROM posts WHERE id = (%s);", (flag_id,))
        self.database.conn.commit()

        return post
