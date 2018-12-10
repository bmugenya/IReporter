from IncidentViews import *
from UserViews import *

from flask_restful import Api, Resource
from flask import Blueprint

version_one = Blueprint('api_v1', __name__, url_prefix='/api/v1')
api = Api(version_one)


api.add_resource(ViewFlags, "/red-flags")
api.add_resource(ViewFlag, "/red-flag/<int:flag_id>")
api.add_resource(RedFlags, "/red-flag")
api.add_resource(UpdateMap, "/red-flag/<int:flag_id>/location")
api.add_resource(UpdatePost, "/red-flag/<int:flag_id>/comment")
api.add_resource(UpdateStatus, "/red-flag/<int:flag_id>/status")
api.add_resource(RemoveFlag, "/red-flag/<int:flag_id>")
api.add_resource(AdminReg, "/auth/register/admin")
api.add_resource(UserReg, "/auth/register/user")
api.add_resource(AdminAcces, "/auth/login/admin")
api.add_resource(UserAcces, "/auth/login/user")
