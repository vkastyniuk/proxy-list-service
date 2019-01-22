from flask import request
from flask_restful import Resource

from proxy_service.api.schemas import proxy_filter_schema, proxy_schema
from proxy_service.services import ProxyService


class ProxiesResource(Resource):
    def __init__(self) -> None:
        super().__init__()
        self.service = ProxyService.get_instance()

    def get(self):
        filters, errors = proxy_filter_schema.load(request.args)
        if errors:
            return errors, 400

        proxies = self.service.get_proxies(**filters)
        return proxy_schema.jsonify(proxies, many=True)

    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400

        proxy, errors = proxy_schema.load(json_data)
        if errors:
            return errors, 400

        proxy = self.service.add_proxy(proxy)
        return proxy_schema.jsonify(proxy)
