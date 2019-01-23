import datetime
import json
import logging

from sqlalchemy import func

from proxy_service.api.models import db, Proxy

LOGGER = logging.getLogger(__name__)


class ProxyService(object):
    _instance = None

    def __init__(self, settings, database=db) -> None:
        self.last_check_threshold = settings.get('LAST_CHECK_THRESHOLD', 5)
        self.db = database

    @classmethod
    def get_instance(cls, settings):
        if not cls._instance:
            LOGGER.debug('Create a new instance of %s', cls.__class__.__name__)
            cls._instance = cls(settings)

        return cls._instance

    def get_proxies(self, **kwargs):
        LOGGER.debug('Get proxy list by parameters: %s', json.dumps(kwargs))

        query = self.db.session.query(Proxy)
        threshold = datetime.datetime.now() - datetime.timedelta(hours=self.last_check_threshold)
        query = query.filter(Proxy.last_check >= threshold)

        proxy_type = kwargs.get('proxy_type')
        if proxy_type:
            query = query.filter(func.lower(Proxy.proxy_type) == func.lower(proxy_type))

        anonymity = kwargs.get('anonymity')
        if anonymity:
            query = query.filter(func.lower(Proxy.anonymity) == func.lower(anonymity))

        country_code = kwargs.get('country_code')
        if country_code:
            query = query.filter(func.lower(Proxy.country_code) == func.lower(country_code))

        port_number = kwargs.get('port_number')
        if port_number:
            query = query.filter(Proxy.port_number == port_number)

        response_time = kwargs.get('response_time')
        if response_time:
            query = query.filter(Proxy.response_time <= response_time)

        last_check = kwargs.get('last_check')
        if last_check:
            query = query.filter(Proxy.last_check >= last_check)

        order_by = kwargs.get('order_by')
        if order_by:
            query = query.order_by('%s %s' % (order_by, kwargs.get('order_dir', 'asc')))

        query = query.order_by('last_check desc')
        query = query.limit(kwargs.get('limit'))
        query = query.offset(kwargs.get('offset'))

        return query.all()

    def add_proxy(self, proxy):
        self.db.session.add(proxy)
        self.db.session.commit()

    def add_proxies(self, proxies):
        for proxy in proxies:
            self.db.session.merge(proxy)

        self.db.session.commit()
