from flask import request, jsonify, make_response
from flask_restful import Resource, Api

from models import FlagModel, reported_flags


class Flags(Resource, FlagModel):
    """docstring for  MyRecords """

    def __init__(self):
        self.db = FlagModel()

    def post(self):
        data = request.get_json()
        title = data["title"]
        flag_type = data["flag_type"]
        location = data["location"]
        incident = data["incident"]
        flags = self.db.save(title, flag_type, location, incident)

        return make_response(jsonify({
            "Reported Flags": flags
        }), 200)

    def get(self):
        flags = self.db.get()

        return make_response(jsonify({
            "Reported Flags": flags
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
