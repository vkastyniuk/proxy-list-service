from flask_restful import reqparse, Resource

from proxy_service.services import ProxyService


class ProxiesResource(Resource):
    proxy_types = ('HTTP', 'HTTPS', 'SOCKS4', 'SOCKS5')
    anonymity_levels = ('HTTP', 'HTTPS', 'SOCKS4', 'SOCKS5')

    parser = reqparse.RequestParser()
    parser.add_argument('proxy_type', type=str, location='args', case_sensitive=False, choices=proxy_types)
    parser.add_argument('anonymity', type=str, location='args', case_sensitive=False, choices=anonymity_levels)
    parser.add_argument('country_code', type=str, location='args')
    parser.add_argument('port_number', type=int, location='args')
    parser.add_argument('response_time', type=int, location='args')
    parser.add_argument('last_check', type=int, location='args')
    parser.add_argument('limit', type=int, location='args', default=50)
    parser.add_argument('offset', type=int, location='args', default=0)

    def get(self):
        kwargs = self.parser.parse_args()
        service = ProxyService.get_instance()
        return service.get_proxies(**kwargs)
