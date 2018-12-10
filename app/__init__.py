from flask import Flask, Blueprint


# local imports
# from instance.config import app_config
from .api.v1 import version_one as v1
from db_con import create_tables


def create_app():

    app = Flask(__name__)
    create_tables()

    app.register_blueprint(v1)
    return app
