import http

from flask import current_app as app
from flask import request
from flask_restful import Resource

from proxy_service.api.schemas import proxy_filter_schema, proxy_schema
from proxy_service.services import ProxyService


class ProxiesResource(Resource):
    def __init__(self) -> None:
        super().__init__()

    def get(self):
        filters, errors = proxy_filter_schema.load(request.args)
        if errors:
            return errors, 400

        service = ProxyService.get_instance(app.config)
        proxies = service.get_proxies(**filters)
        return proxy_schema.jsonify(proxies, many=True)

    def put(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400

        proxy, errors = proxy_schema.load(json_data)
        if errors:
            return errors, 400

        service = ProxyService.get_instance(app.config)
        service.add_proxy(proxy)
        return '', http.HTTPStatus.NO_CONTENT


class ProxiesBatchResource(Resource):

    def put(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400

        proxies, errors = proxy_schema.load(json_data, many=True)
        if errors:
            return errors, 400

        service = ProxyService.get_instance(app.config)
        service.add_proxies(proxies)
        return '', http.HTTPStatus.NO_CONTENT
