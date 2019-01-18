import os

SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s?sslmode=%(sslmode)s&sslrootcert=%(sslrootcert)s' % {
    'user': os.getenv('POSTGRES_USERNAME', 'postgres'),
    'pw': os.getenv('POSTGRES_PASSWORD', 'postgres'),
    'db': os.getenv('POSTGRES_DB', 'proxy-list'),
    'host': os.getenv('POSTGRES_HOST', 'localhost'),
    'sslmode': os.getenv('POSTGRES_SSL_MODE', 'disable'),
    'sslrootcert': os.getenv('POSTGRES_SSL_ROOT_CERT', ''),
    'port': '5432',
}
