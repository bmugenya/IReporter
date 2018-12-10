from flask import request, jsonify, make_response
from flask_restful import Resource

from incident import *
from users import *


class RedFlags(Resource, PostIncidents):

    def __init__(self):
        self.incident = PostIncidents()

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


class ViewFlags(Resource, ViewIncidents):

    def __init__(self):
        self.incident = ViewIncidents()

    def get(self):
        flags = self.incident.get()

        return make_response(jsonify({
            "data": flags
        }), 200)


class ViewFlag(Resource, ViewIncident):

    def __init__(self):
        self.incident = ViewIncident()

    def get(self, flag_id):
        flag = self.incident.get_flag(flag_id)
        return make_response(jsonify({
            "Reported Flags": flag
        }), 200)


class UpdateMap(Resource, UpdateIncident):

    def __init__(self):
        self.incident = UpdateIncident()

    def patch(self, flag_id):
        data = request.get_json()
        location = data["location"]
        updated = self.incident.update_map(flag_id, location)

        return make_response(jsonify({
            "Reported Flags": updated
        }), 200)


class UpdatePost(Resource, UpdateIncident):

    def __init__(self):
        self.incident = UpdateIncident()

    def patch(self, flag_id):
        data = request.get_json()
        comment = data["comment"]
        updated = self.incident.update_post(flag_id, comment)

        return make_response(jsonify({
            "Reported Flags": updated
        }), 200)


class UpdateStatus(Resource, UpdateIncident):

    def __init__(self):
        self.incident = UpdateIncident()

    def patch(self, flag_id):
        data = request.get_json()
        status = data["status"]
        updated = self.incident.update_status(flag_id, status)

        return make_response(jsonify({
            "Reported Flags": updated
        }), 200)


class RemoveFlag(Resource, RemoveIncident):
    def __init__(self):
        self.incident = RemoveIncident()

    def delete(self, flag_id):
        resp = self.incident.remove_data(flag_id)
        return make_response(jsonify({
            "deleted": resp
        }), 200)


class AdminReg(Resource, AdminRegistration):
    def __init__(self):
        self.user = AdminRegistration()

    def post(self):
        data = request.get_json()
        firstname = data["firstname"]
        lastname = data["lastname"]
        othernames = data["othernames"]
        email = data["email"]
        phoneNumber = data["phoneNumber"]
        username = data["username"]
        password = data["password"]

        users = self.user.save_admin(firstname, lastname, othernames, email, phoneNumber, username, password)

        return make_response(jsonify({
            "Admin created": users
        }), 201)


class UserReg(Resource, UserRegistration):
    def __init__(self):
        self.user = UserRegistration()

    def post(self):
        data = request.get_json()
        firstname = data["firstname"]
        lastname = data["lastname"]
        othernames = data["othernames"]
        email = data["email"]
        phoneNumber = data["phoneNumber"]
        username = data["username"]
        password = data["password"]

        users = self.user.save_user(firstname, lastname, othernames, email, phoneNumber, username, password)

        return make_response(jsonify({
            "User created": users
        }), 201)


class AdminAcces(Resource, AdminLogin):
    def __init__(self):
        self.user = AdminLogin()

    def post(self):
        data = request.get_json()
        email = data["email"]
        password = data["password"]
        users = self.user.login(email, password)

        return make_response(jsonify({
            "Welcome": users
        }), 201)


class UserAcces(Resource, UserLogin):
    def __init__(self):
        self.user = UserLogin()

    def post(self):
        data = request.get_json()
        email = data["email"]
        password = data["password"]
        users = self.user.login(email, password)

        return make_response(jsonify({
            "Welcome": users
        }), 201)
