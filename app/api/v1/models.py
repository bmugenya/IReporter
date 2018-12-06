from datetime import datetime

reported_flags = []
visit = []


class FlagModel():

    def __init__(self):

        self.db = reported_flags
        self.users = visit

    def save(self, flag_type, location, incident):

        self.time = datetime.now()
        flag_id = len(self.db) + 1
        created_on = self.time

        flag = {
            "id": flag_id,
            "createdOn": created_on,
            "createdBy": flag_id,
            "type": flag_type,
            "location": location,
            "status": "pending",
            "photo": "bribe.jpg",
            "video": "bribe.mp4",
            "comments": incident

        }

        self.db.append(flag)
        return self.db

    def get(self):
        return self.db

    def get_flag(self, post_id):
        for post in self.db:
            if post_id == post['id']:
                return post, 200
        return "Post not found", 404

    def update_flag(self, flag_id, data):
        for post in self.db:
            if post["id"] == flag_id:
                post.update(data)
                return post

    def remove_data(self, flag_id):
        for post in self.db:
            if post["id"] == flag_id:
                self.db.remove(post)
                return self.db

    def save_user(self, firstname, lastname, othernames, email, phoneNumber, username):

        time = datetime.now()
        user_id = len(self.db) + 1

        user = {
            "id": user_id,
            "firstname": firstname,
            "lastname": lastname,
            "othernames": othernames,
            "email": email,
            "phoneNumber": phoneNumber,
            "username": username,
            "registered": time,
            "isAdmin": False,

        }

        self.users.append(user)
        return self.users
