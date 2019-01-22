from datetime import datetime

from flask_marshmallow import Marshmallow
from marshmallow import fields, validate

from proxy_service.api.models import Proxy, db

proxy_types = ('HTTP', 'HTTPS', 'SOCKS4', 'SOCKS5')
anonymity_levels = ('High', 'Medium', 'Low', 'No')

ma = Marshmallow()


class UnixTimestamp(fields.DateTime):

    def _serialize(self, value, attr, obj):
        if value is None:
            return None

        try:
            return value.timestamp()
        except (AttributeError, ValueError):
            self.fail('format', input=value)

    def _deserialize(self, value, attr, data):
        if not value:
            raise self.fail('invalid')

        try:
            return datetime.fromtimestamp(value)
        except (TypeError, AttributeError, ValueError):
            raise self.fail('invalid')


class ProxySchema(ma.ModelSchema):
    class Meta:
        model = Proxy

    proxy_type = fields.String(required=True, validate=validate.OneOf(proxy_types))
    last_check = UnixTimestamp()
    anonymity = fields.String(validate=validate.OneOf(anonymity_levels))


class ProxyFilterSchema(ma.Schema):
    port_number = fields.Integer()
    proxy_type = fields.String(validate=validate.OneOf(proxy_types))
    response_time = fields.Integer()
    last_check = UnixTimestamp()
    anonymity = fields.String(validate=validate.OneOf(anonymity_levels))
    country_code = fields.String()

    order_by = fields.String(missing='response_time')
    order_dir = fields.String(missing='desc')
    limit = fields.Integer(missing=50)
    offset = fields.Integer(missing=0)


proxy_schema = ProxySchema(session=db.session)
proxy_filter_schema = ProxyFilterSchema()
