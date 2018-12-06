from views import Flags, SingleFlag, FlagUpdate, FlagRemove, User

from flask_restful import Api, Resource
from flask import Blueprint

version_one = Blueprint('api_v1', __name__, url_prefix='/api/v1')
api = Api(version_one)

api.add_resource(Flags, "/record")
api.add_resource(SingleFlag, "/record/<int:flag_id>")
api.add_resource(FlagUpdate, "/record/<int:flag_id>")
api.add_resource(FlagRemove, "/record/<int:flag_id>")
api.add_resource(User, "/user")
