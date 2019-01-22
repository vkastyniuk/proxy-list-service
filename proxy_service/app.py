from flask import Flask
from flask_migrate import Migrate

from proxy_service import config
from proxy_service.api import blueprint
from proxy_service.api.models import db
from proxy_service.api.schemas import ma

__all__ = ('create_app',)


def create_app(config_obj=config):
    flask = Flask(__name__)

    # setup configuration
    flask.config.from_object(config_obj)

    # register blueprint
    flask.register_blueprint(blueprint)

    # setup extensions
    db.init_app(flask)
    ma.init_app(flask)

    migrate = Migrate()
    migrate.init_app(flask, db)

    return flask
