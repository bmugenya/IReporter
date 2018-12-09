from flask import request, jsonify, make_response, json
from flask_restful import Resource, Api

from incident import Incident
from users import User


class Flags(Resource, Incident):

    def __init__(self):
        self.incident = Incident()

    def post(self):
        data = request.get_json()
        post_type = data["post_type"]
        location = data["location"]
        comment = data["comment"]
        flags = self.incident.save(post_type, location, comment)

        return make_response(jsonify({
            "data": flags,
            'message': 'Successfully created red flag'
        }), 201)

    def get(self):
        flags = self.incident.get()

        return make_response(jsonify({
            "data": flags
        }), 200)


class SingleFlag(Resource, Incident):

    def __init__(self):
        self.incident = Incident()

    def get(self, flag_id):
        flag = self.incident.get_flag(flag_id)
        return make_response(jsonify({
            "Reported Flags": flag
        }), 200)


class FlagUpdate(Resource, Incident):

    def __init__(self):
        self.incident = Incident()

    def patch(self, flag_id):
        data = request.get_json()
        post_type = data["post_type"]
        location = data["location"]
        comment = data["comment"]
        updated = self.incident.update_flag(flag_id, post_type, location, comment)

        return make_response(jsonify({
            "Reported Flags": updated
        }), 200)


class FlagRemove(Resource, Incident):
    def __init__(self):
        self.incident = Incident()

    def delete(self, flag_id):
        resp = self.incident.remove_data(flag_id)
        return make_response(jsonify({
            "deleted": resp
        }), 200)


class Users(Resource, User):
    def __init__(self):
        self.user = User()

    def post(self):
        data = request.get_json()
        firstname = data["firstname"]
        lastname = data["lastname"]
        othernames = data["othernames"]
        email = data["email"]
        phoneNumber = data["phoneNumber"]
        username = data["username"]
        passwrd = data["password"]

        users = self.user.save_user(firstname, lastname, othernames, email, phoneNumber, username, passwrd)

        return make_response(jsonify({
            "User created": users
        }), 201)
