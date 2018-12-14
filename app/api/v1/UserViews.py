from flask import request, jsonify, make_response
from flask_restful import Resource


from users import *


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

        admin = self.user.save_admin(firstname, lastname, othernames, email, phoneNumber, username, password)

        return make_response(jsonify({
            "Admin": admin,
            'message': 'Success'

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
            "User created": users,
            'message': 'Success'
        }), 201)


class AdminAcces(Resource, AdminLogin):
    def __init__(self):
        self.user = AdminLogin()

    def post(self):
        data = request.get_json()
        email = data["email"]
        password = data["password"]
        admin = self.user.login(email, password)

        return make_response(jsonify({
            "Welcome": admin,
            'message': 'Success'

        }), 200)


class UserAcces(Resource, UserLogin):
    def __init__(self):
        self.user = UserLogin()

    def post(self):
        data = request.get_json()
        email = data["email"]
        password = data["password"]
        users = self.user.login(email, password)

        return make_response(jsonify({
            "Welcome": users,
            'message': 'Success'

        }), 200)
