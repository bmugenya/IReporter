from ...db_con import init_db


class PostIncidents():

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


class ViewIncidents():
    def __init__(self):
        self.incident = init_db()

    def get(self):
        curr = self.incident.cursor()
        curr.execute("SELECT * FROM Posts")
        post = curr.fetchall()
        return post


class ViewIncident():

    def __init__(self):
        self.incident = init_db()

    def get_flag(self, flag_id):
        curr = self.incident.cursor()
        curr.execute("SELECT * FROM Posts WHERE id = (%s);", (flag_id,))

        post = curr.fetchall()
        return post


class UpdateIncident():

    def __init__(self):
        self.incident = init_db()

    def update_map(self, flag_id, location):
        curr = self.incident.cursor()
        post = {
            "location": location,
        }
        query = "UPDATE Posts SET location= '%s' WHERE id = %s;" % (location, flag_id)
        curr.execute(query, post)

        self.incident.commit()
        return post

    def update_post(self, flag_id, comment):
        curr = self.incident.cursor()
        post = {
            "comment": comment,
        }
        query = "UPDATE Posts SET comments= '%s' WHERE id = %s;" % (comment, flag_id)
        curr.execute(query, post)

        self.incident.commit()
        return post

    def update_status(self, flag_id, status):
        curr = self.incident.cursor()
        post = {
            "status": status,
        }
        query = "UPDATE Posts SET status= '%s' WHERE id = %s;" % (status, flag_id)
        curr.execute(query, post)

        self.incident.commit()
        return post


class RemoveIncident():

    def __init__(self):
        self.incident = init_db()

    def remove_data(self, flag_id):
        curr = self.incident.cursor()
        post = curr.execute("DELETE FROM posts WHERE id = (%s);", (flag_id,))
        self.incident.commit()

        return post
