from flask import Flask
from flask_restful import Api, Resource

# local imports
from .api.v1.views import Flags, SingleFlag
# from instance.config import app_config


# def create_app(config_name):
def create_app():
           # app = Flask(__name__, instance_relative_config=True)
    app = Flask(__name__)
    # app.config.from_object(app_config[config_name])
    # app.config.from_pyfile('config.py')
    api = Api(app)
    api.add_resource(Flags, "/record")
    api.add_resource(SingleFlag, "/record/<int:flag_id>")

    return app


#  for proc file - web:gunicorn run:app
