from flask import request, jsonify, make_response, json
from flask_restful import Resource, Api

from models import FlagModel


class Flags(Resource, FlagModel):

    def __init__(self):
        self.db = FlagModel()

    def post(self):
        data = request.get_json()
        incident = data["incident"]
        location = data["location"]
        comment = data["comment"]
        flags = self.db.save(incident, location, comment)

        return make_response(jsonify({
            "data": flags,
            'message': 'Successfully created red flag'
        }), 201)

    def get(self):
        flags = self.db.get()

        return make_response(jsonify({
            "data": flags
        }), 200)


class SingleFlag(Resource, FlagModel):
    """docstring for  MyRecords """

    def __init__(self):
        self.db = FlagModel()

    def get(self, flag_id):
        flag = self.db.get_flag(flag_id)
        return make_response(jsonify({
            "Reported Flags": flag
        }), 200)


class FlagUpdate(Resource, FlagModel):
    """docstring for  MyRecords """

    def __init__(self):
        self.db = FlagModel()

    def patch(self, flag_id):
        data = request.get_json()
        incident = data["incident"]
        location = data["location"]
        comment = data["comment"]
        updated = self.db.update_flag(flag_id, incident, location, comment)

        return make_response(jsonify({
            "Reported Flags": updated
        }), 200)


class User(Resource, FlagModel):
    def __init__(self):
        self.user = FlagModel()

    def post(self):
        data = request.get_json()
        firstname = data["firstname"]
        lastname = data["lastname"]
        othernames = data["othernames"]
        email = data["email"]
        phoneNumber = data["phoneNumber"]
        username = data["username"]

        users = self.user.save_user(firstname, lastname, othernames, email, phoneNumber, username)

        return make_response(jsonify({
            "User created": users
        }), 201)


class FlagRemove(Resource, FlagModel):
    """docstring for  MyRecords """

    def __init__(self):
        self.db = FlagModel()

    def delete(self, flag_id):
        resp = self.db.remove_data(flag_id)
        return make_response(jsonify({
            "deleted": resp
        }), 200)
