from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Proxy(db.Model):
    __tablename__ = 'proxies'

    ip_address = db.Column(db.String, primary_key=True)
    port_number = db.Column(db.Integer, primary_key=True)
    country_code = db.Column(db.String)
    country = db.Column(db.String)
    city = db.Column(db.String)
    response_time = db.Column(db.Integer, nullable=False)
    proxy_type = db.Column(db.String, nullable=False)
    anonymity = db.Column(db.String, nullable=False)
    last_check = db.Column(db.TIMESTAMP, nullable=False)
