from views import Flags, SingleFlag, FlagUpdate, FlagRemove

from flask_restful import Api, Resource
from flask import Blueprint

version_two = Blueprint('api_v2', __name__, url_prefix='/api/v2')
api = Api(version_two)

api.add_resource(Flags, "/record")
api.add_resource(SingleFlag, "/record/<int:flag_id>")
api.add_resource(FlagUpdate, "/record/<int:flag_id>")
api.add_resource(FlagRemove, "/record/<int:flag_id>")
