import json
import logging

from proxy_service.api.models import db, Proxy

LOGGER = logging.getLogger(__name__)


class ProxyService(object):
    _instance = None

    def __init__(self, database=db) -> None:
        self.db = database

    @classmethod
    def get_instance(cls):
        if not cls._instance:
            LOGGER.debug('Create a new instance of %s', cls.__class__.__name__)
            cls._instance = cls()

        return cls._instance

    def get_proxies(self, **kwargs):
        LOGGER.debug('Get proxy list by parameters: %s', json.dumps(kwargs))

        query = self.db.session.query(Proxy)
        proxy_type = kwargs.get('proxy_type')
        if proxy_type:
            query = query.filter(Proxy.proxy_type == proxy_type)

        anonymity = kwargs.get('anonymity')
        if anonymity:
            query = query.filter(Proxy.anonymity == anonymity)

        country_code = kwargs.get('country_code')
        if country_code:
            query = query.filter(Proxy.country_code == country_code)

        port_number = kwargs.get('port_number')
        if port_number:
            query = query.filter(Proxy.port_number == port_number)

        response_time = kwargs.get('response_time')
        if response_time:
            query = query.filter(Proxy.response_time <= response_time)

        last_check = kwargs.get('last_check')
        if last_check:
            query = query.filter(Proxy.last_check >= last_check)

        query = query.order_by('%s %s' % (kwargs.get('order_by'), kwargs.get('order_dir')))
        query = query.limit(kwargs.get('limit'))
        query = query.offset(kwargs.get('offset'))

        return query.all()

    def add_proxy(self, proxy):
        self.db.session.merge(proxy)
        self.db.session.commit()
        return proxy
