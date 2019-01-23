from flask import Blueprint
from flask_restful import Api

from proxy_service.api.resources import ProxiesResource, ProxiesBatchResource

blueprint = Blueprint('api', __name__, url_prefix='/api')
api = Api(blueprint)

# register resources
api.add_resource(ProxiesResource, '/proxies')
api.add_resource(ProxiesBatchResource, '/proxies/batch')
