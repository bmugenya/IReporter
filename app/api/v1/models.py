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
