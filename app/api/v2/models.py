#   commands
# sudo -i -u postgres - to switch to a postgres server
# psql - to acces a postgres prompt
# createuser --interactive - to create a new user
# createdb (name of createduser)
#  sudo -u mugenya psql - connect to db
# \coninfo - check current connection


# \q - to quit
import psycopg2
DBNAME = "mugenya"


class FlagModel():

    def __init__(self):

        self.db = reported_flags

    def save(self, title, flag_type, location, incident):

        self.time = datetime.now()
        flag_id = len(self.db) + 1
        created_on = self.time

        db = psycopg2.connect(database=DBNAME)
        c = db.cursor()
        c.exectute(
        )

        return c.fetchall(" insert into post values(%"Id": flag_id,
            "Title": title,
            "Type": flag_type,
            "location": location,
            "Incident": incident,
            "Date": created_on
")
        db.close()



    def get(self):
        db = psycopg2.connect(database=DBNAME)
        c = db.cursor()
        c.exectute(
        )
        return c.fetchall()
        db.close()

    def get_flag(self, post_id):
        for post in self.db:
            if post_id == post['Id']:
                return post, 200
        return "Post not found", 404

    def update_flag(self, flag_id, data):
        for post in self.db:
            if post["Id"] == flag_id:
                post.update(data)
                return post

    def remove_data(self):
        for redflag in reported_flags:
            item = self.db
            self.db.remove(item)
            return self.db
