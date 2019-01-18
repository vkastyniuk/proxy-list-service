from flask import Blueprint
from flask_restful import Api

from proxy_service.api.resources import ProxiesResource

blueprint = Blueprint('api', __name__, url_prefix='/api')
api = Api(blueprint)

# register resources
api.add_resource(ProxiesResource, '/proxies')
