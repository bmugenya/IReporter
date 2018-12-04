from datetime import datetime

reported_flags = []


class FlagModel():

    def __init__(self):

        self.db = reported_flags

    def save(self, title, flag_type, location, incident):

        self.time = datetime.now()
        flag_id = len(self.db) + 1
        created_on = self.time

        flag = {
            "Id": flag_id,
            "Title": title,
            "Type": flag_type,
            "location": location,
            "Incident": incident,
            "Date": created_on

        }

        self.db.append(flag)
        return self.db

    def get(self):
        return self.db

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

    def remove_data(self, flag_id):
        for post in self.db:
            if post["Id"] == flag_id:
                post.remove(data)
                return self.db
