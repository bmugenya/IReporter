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
