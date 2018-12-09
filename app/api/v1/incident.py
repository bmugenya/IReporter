from ...db_con import init_db


class Incident():

    def __init__(self):
        self.incident = init_db()

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
        curr = self.incident.cursor()
        curr.execute(query, post)
        self.incident.commit()

        return post

    def get(self):
        curr = self.incident.cursor()
        curr.execute("SELECT * FROM Posts")
        post = curr.fetchall()
        return post

    def get_flag(self, flag_id):
        curr = self.incident.cursor()
        curr.execute("SELECT * FROM Posts WHERE id = (%s);", (flag_id,))

        post = curr.fetchall()
        return post

    def update_flag(self, flag_id, post_type, location, comment):
        curr = self.incident.cursor()
        post = {
            "post_type": post_type,
            "location": location,
            "comment": comment

        }
        query = "UPDATE Posts SET post_type= '%s',location= '%s', comments='%s' WHERE id = %s;" % (post_type, location, comment, flag_id)
        curr.execute(query, post)

        self.incident.commit()
        return post

    def remove_data(self, flag_id):
        curr = self.incident.cursor()
        post = curr.execute("DELETE FROM posts WHERE id = (%s);", (flag_id,))
        self.incident.commit()

        return post
